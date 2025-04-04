<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

    <xsl:template match="article-meta/contrib-group" mode="sub-article-not-translation-component">
        <xsl:apply-templates select="." mode="contrib-group">
            <xsl:with-param name="id"><xsl:value-of select="../../../@id"/></xsl:with-param>
        </xsl:apply-templates>
        <xsl:if test="..//aff">
            <xsl:apply-templates select=".." mode="scimago-button">
                <xsl:with-param name="id"><xsl:value-of select="../../../@id"/></xsl:with-param>
            </xsl:apply-templates>
        </xsl:if>
    </xsl:template>

    <xsl:template match="front-stub/contrib-group" mode="sub-article-not-translation-component">
        <xsl:apply-templates select="." mode="contrib-group">
            <xsl:with-param name="id"><xsl:value-of select="../../@id"/></xsl:with-param>
        </xsl:apply-templates>
        <xsl:if test="..//aff">
            <xsl:apply-templates select=".." mode="scimago-button">
                <xsl:with-param name="id"><xsl:value-of select="../../@id"/></xsl:with-param>
            </xsl:apply-templates>
        </xsl:if>
    </xsl:template>

    <xsl:template match="article" mode="article-meta-contrib">
        <xsl:choose>
            <xsl:when
                test="sub-article[@article-type='translation' and @xml:lang=$TEXT_LANG]">
                <xsl:apply-templates
                    select="sub-article[@article-type='translation' and @xml:lang=$TEXT_LANG]" mode="contrib-group"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="." mode="contrib-group"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="article | sub-article" mode="contrib-group">
        <div>
            <xsl:attribute name="class">contribGroup</xsl:attribute>
            <xsl:apply-templates select="front | front-stub" mode="contrib-group"/>
        </div>
    </xsl:template>

    <xsl:template match="front | front-stub" mode="contrib-group">
        <xsl:variable name="id"><xsl:value-of select="../@id"/></xsl:variable>
        <xsl:apply-templates select=".//contrib-group[1]" mode="contrib-group">
            <xsl:with-param name="id"><xsl:value-of select="$id"/></xsl:with-param>
        </xsl:apply-templates>
        <xsl:apply-templates select="." mode="scimago-button">
            <xsl:with-param name="id"><xsl:value-of select="$id"/></xsl:with-param>
        </xsl:apply-templates>

        <xsl:if test="not(.//contrib-group) and ../@article-type='translation'">
            <!-- obtém o front ou front-stub do parent de sub-article -->
            <xsl:apply-templates select="../../front" mode="contrib-group"/>
            <xsl:apply-templates select="../../front-stub" mode="contrib-group"/>
        </xsl:if>
    </xsl:template>
        
    <xsl:template match="contrib-group" mode="contrib-group">
        <xsl:param name="id"/>
        <!--
            Remove a apresentação dos autores, deixando apenas o botão "sobre os autores
        <xsl:apply-templates select="contrib[@contrib-type='author']" mode="article-meta-contrib"/>
        -->
        <xsl:apply-templates select="." mode="about-the-contrib-group-button">
            <xsl:with-param name="id"><xsl:value-of select="$id"/></xsl:with-param>
        </xsl:apply-templates>
    </xsl:template>

    <xsl:template match="contrib-group" mode="about-the-contrib-group-button">
        <xsl:param name="id"/>
        <!--
            Adiciona o botão 'About the contributor', trocando 'author',
            pelo tipo de contribuição
        -->
        <xsl:if test="contrib/*[name()!='name' and name()!='collab']">
            <a href="" class="outlineFadeLink" data-toggle="modal"
                data-target="#ModalTutors{$id}">
                <xsl:apply-templates select="." mode="about-the-contrib-group-button-text"/>
            </a>
        </xsl:if>
    </xsl:template>

    <xsl:template match="front | front-stub" mode="scimago-button">
        <xsl:param name="id"/>
        <!--
            Adiciona o botão 'SCIMAGO INSTITUTIONS RANKINGS'
        -->
        <xsl:if test=".//aff">
            <a href="" class="outlineFadeLink" data-toggle="modal"
                data-target="#ModalScimago{$id}">
                SCIMAGO INSTITUTIONS RANKINGS
            </a>
        </xsl:if>
    </xsl:template>
    
    <xsl:template match="article-meta/contrib-group | front/contrib-group | front-stub/contrib-group" mode="about-the-contrib-group-button-text">
        <xsl:variable name="type">
            <xsl:choose>
                <xsl:when test="../../@article-type='reviewer-report'">reviewer</xsl:when>
                <xsl:otherwise><xsl:value-of select="contrib[1]/@contrib-type"/></xsl:otherwise>
            </xsl:choose>
        </xsl:variable>
        <xsl:variable name="count"><xsl:value-of select="count(contrib[@contrib-type=$type])"/></xsl:variable>

        <xsl:apply-templates select="." mode="interface">
            <xsl:with-param name="text">About the <xsl:value-of select="$type"/><xsl:if test="number($count)&gt;1">s</xsl:if></xsl:with-param>
        </xsl:apply-templates>
    </xsl:template>
   
    <!--xsl:template match="contrib" mode="article-meta-contrib">
        <xsl:choose>
            <xsl:when test="*[name()!='name' and name()!='collab']">
                <xsl:variable name="id">
                    <xsl:value-of select="position()"/>
                </xsl:variable>
                <span class="dropdown">
                    <a id="contribGroupTutor{$id}">
                        <xsl:attribute name="class">dropdown-toggle</xsl:attribute>
                        <xsl:attribute name="data-toggle">dropdown</xsl:attribute>
                        <span>
                            <xsl:choose>
                                <xsl:when test="$ABBR_CONTRIB='true'">
                                    <xsl:apply-templates select="name|collab|on-behalf-of" mode="abbrev"/>
                                </xsl:when>
                                <xsl:otherwise><xsl:apply-templates select="name|collab|on-behalf-of"/></xsl:otherwise>
                            </xsl:choose>
                        </span>
                    </a>
                    <xsl:apply-templates select="." mode="contrib-dropdown-menu">
                        <xsl:with-param name="id">
                            <xsl:value-of select="$id"/>
                        </xsl:with-param>
                    </xsl:apply-templates>
                </span>
            </xsl:when>
            <xsl:otherwise>
                <span class="dropdown"><span>
                    <xsl:choose>
                        <xsl:when test="$ABBR_CONTRIB='true'">
                            <xsl:apply-templates select="name|collab|on-behalf-of" mode="abbrev"/>
                        </xsl:when>
                        <xsl:otherwise><xsl:apply-templates select="name|collab|on-behalf-of"/></xsl:otherwise>
                    </xsl:choose>
                </span></span>
            </xsl:otherwise>
        </xsl:choose>
        
    </xsl:template-->

    <xsl:template match="contrib" mode="article-meta-contrib">
        <xsl:variable name="id">
            <xsl:value-of select="position()"/>
        </xsl:variable>
        <span class="dropdown">
            <a id="contribGroupTutor{$id}">
                <xsl:attribute name="class">dropdown-toggle</xsl:attribute>
                <xsl:attribute name="data-toggle">dropdown</xsl:attribute>
                <span>
                    <xsl:choose>
                        <xsl:when test="$ABBR_CONTRIB='true'">
                            <xsl:apply-templates select="name|collab|on-behalf-of" mode="abbrev"/>
                        </xsl:when>
                        <xsl:otherwise><xsl:apply-templates select="name|collab|on-behalf-of"/></xsl:otherwise>
                    </xsl:choose>
                </span>
            </a>
            <xsl:apply-templates select="." mode="contrib-dropdown-menu">
                <xsl:with-param name="id">
                    <xsl:value-of select="$id"/>
                </xsl:with-param>
            </xsl:apply-templates>
        </span>
    </xsl:template>

    <xsl:template match="sub-article[@article-type!='translation']//contrib" mode="article-meta-contrib">
        <span class="dropdown"> 
            <xsl:if test="position() != 1"><span> • </span></xsl:if>
            <span>
                <xsl:choose>
                    <xsl:when test="$ABBR_CONTRIB='true'">
                        <xsl:apply-templates select="name|collab|on-behalf-of" mode="abbrev"/>
                    </xsl:when>
                    <xsl:otherwise><xsl:apply-templates select="name|collab|on-behalf-of"/></xsl:otherwise>
                </xsl:choose>
            </span>
            
        </span>
    </xsl:template>

    <xsl:template match="contrib/role | contrib/bio">
        <div>
            <xsl:apply-templates select="*|text()"></xsl:apply-templates>
        </div>
    </xsl:template>
    
    <xsl:template match="contrib" mode="contrib-dropdown-menu">
        <xsl:param name="id"/>
        <xsl:if test="role or xref or contrib-id or bio">
            <ul class="dropdown-menu" role="menu" aria-labelledby="contribGrupoTutor{$id}">
                <strong></strong>
                <xsl:apply-templates select="role | bio"/>
                <xsl:apply-templates select="xref" mode="contrib-dropdown-menu"/>
                <xsl:apply-templates select="contrib-id"/>
            </ul>
        </xsl:if>
    </xsl:template>
    
    <xsl:template match="contrib/xref" mode="contrib-dropdown-menu">
        <xsl:variable name="rid" select="@rid"/>
        <xsl:apply-templates select="$article//author-notes/corresp[@id=$rid]" mode="contrib-dropdown-menu"/>
            <xsl:apply-templates select="$article//aff[@id=$rid]" mode="contrib-dropdown-menu"/>
        <xsl:apply-templates select="$article//fn[@id=$rid]" mode="xref"/>
    </xsl:template>
    
    <xsl:template match="aff" mode="contrib-dropdown-menu">
            <xsl:apply-templates select="." mode="display"/>
    </xsl:template>

    <xsl:template match="contrib/name">
        <xsl:apply-templates select="prefix"/>
        <xsl:text> </xsl:text>
        <xsl:apply-templates select="given-names"/>
        <xsl:text> </xsl:text>
        <xsl:apply-templates select="surname"/>
        <xsl:text> </xsl:text>
        <xsl:apply-templates select="suffix"/>
    </xsl:template>
    
    <xsl:template match="contrib/name" mode="abbrev">
        <xsl:value-of select="substring(given-names,1,1)"/>
        <xsl:text> </xsl:text>
        <xsl:apply-templates select="surname"/>
        <xsl:text> </xsl:text>
        <xsl:apply-templates select="suffix"/>
    </xsl:template>
    
    <xsl:template match="contrib-id">
        <xsl:variable name="url">
            <xsl:apply-templates select="." mode="url"/>
        </xsl:variable>
        <xsl:variable name="location">
            <xsl:value-of select="$url"/>
            <xsl:value-of select="."/>
        </xsl:variable>
        <a href="{$location}" class="btnContribLinks {@contrib-id-type}">
            <xsl:value-of select="$location"/>
        </a>
    </xsl:template>

    <xsl:template match="contrib-id" mode="url"/>
    <xsl:template match="contrib-id[@contrib-id-type='orcid']" mode="url"
        >https://orcid.org/</xsl:template>
    <xsl:template match="contrib-id[@contrib-id-type='lattes']" mode="url"
        >https://lattes.cnpq.br/</xsl:template>
    <xsl:template match="contrib-id[@contrib-id-type='scopus']" mode="url"
        >https://www.scopus.com/authid/detail.uri?authorId=</xsl:template>
    <xsl:template match="contrib-id[@contrib-id-type='researchid']" mode="url"
        >https://www.researcherid.com/rid/</xsl:template>

    <xsl:template match="aff" mode="insert-separator">
        <xsl:apply-templates select="institution" mode="insert-separator"/>
        <xsl:apply-templates select="addr-line/*" mode="insert-separator"/>
        <xsl:apply-templates select="country" mode="insert-separator"/>
    </xsl:template>

    <xsl:template match="aff/institution" mode="insert-separator"><xsl:if test="position()!=1">, </xsl:if><xsl:value-of select="."/></xsl:template>

    <xsl:template match="aff/addr-line/* | aff/country" mode="insert-separator">, <xsl:value-of select="."/></xsl:template>
    
    <xsl:template match="aff" mode="display">
        <xsl:choose>
            <xsl:when test="institution[@content-type='original']">
                <xsl:apply-templates select="institution[@content-type='original']"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:apply-templates select="." mode="insert-separator"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    <xsl:template match="role">
        <xsl:if test="position()!=1">, </xsl:if><xsl:apply-templates select="*|text()"></xsl:apply-templates>
    </xsl:template>
</xsl:stylesheet>
