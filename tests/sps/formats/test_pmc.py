import unittest
from lxml import etree as ET
from packtools.sps.utils import xml_utils

from packtools.sps.formats.pmc import (
    xml_pmc_aff,
    xml_pmc_ref,
)


class PipelinePmc(unittest.TestCase):

    def test_xml_pmc_aff(self):
        self.maxDiff = None
        expected = (
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '<xref ref-type="aff" rid="aff1">'
            '<sup>1</sup>'
            '</xref>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            '<label>1</label>'
            'Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'

        )
        xml_tree = ET.fromstring(
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '<xref ref-type="aff" rid="aff1">'
            '<sup>1</sup>'
            '</xref>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            '<label>1</label>'
            '<institution content-type="original">Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.</institution>'
            '<institution content-type="orgname">Universidade Federal do Rio Grande do Sul</institution>'
            '<institution content-type="orgdiv1">Escola de Enfermagem</institution>'
            '<institution content-type="orgdiv2">Programa de Pós-Graduação em Enfermagem</institution>'
            '<addr-line>'
            '<named-content content-type="city">Porto Alegre</named-content>'
            '<named-content content-type="state">RS</named-content>'
            '</addr-line>'
            '<country country="BR">Brazil</country>'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'
        )

        xml_pmc_aff(xml_tree)

        obtained = ET.tostring(xml_tree, encoding="utf-8").decode("utf-8")

        self.assertEqual(obtained, expected)

    def test_xml_pmc_aff_without_xref(self):
        self.maxDiff = None
        expected = (
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            '<label>1</label>'
            'Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'

        )
        xml_tree = ET.fromstring(
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            '<label>1</label>'
            '<institution content-type="original">Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.</institution>'
            '<institution content-type="orgname">Universidade Federal do Rio Grande do Sul</institution>'
            '<institution content-type="orgdiv1">Escola de Enfermagem</institution>'
            '<institution content-type="orgdiv2">Programa de Pós-Graduação em Enfermagem</institution>'
            '<addr-line>'
            '<named-content content-type="city">Porto Alegre</named-content>'
            '<named-content content-type="state">RS</named-content>'
            '</addr-line>'
            '<country country="BR">Brazil</country>'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'
        )

        xml_pmc_aff(xml_tree)

        obtained = ET.tostring(xml_tree, encoding="utf-8").decode("utf-8")

        self.assertEqual(obtained, expected)

    def test_xml_pmc_aff_without_label(self):
        self.maxDiff = None
        expected = (
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '<xref ref-type="aff" rid="aff1">'
            '<sup>1</sup>'
            '</xref>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            'Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'

        )
        xml_tree = ET.fromstring(
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<front>'
            '<article-meta>'
            '<article-id specific-use="scielo-v3" pub-id-type="publisher-id">ZwzqmpTpbhTmtwR9GfDzP7c</article-id>'
            '<article-id specific-use="scielo-v2" pub-id-type="publisher-id">S0080-62342022000100445</article-id>'
            '<article-id pub-id-type="doi">10.1590/1980-220X-REEUSP-2021-0569en</article-id>'
            '<article-id pub-id-type="other">00445</article-id>'
            '<contrib-group>'
            '<contrib contrib-type="author">'
            '<contrib-id contrib-id-type="orcid">0000-0003-0843-6485</contrib-id>'
            '<name>'
            '<surname>Boni</surname>'
            '<given-names>Fernanda Guarilha</given-names>'
            '</name>'
            '<xref ref-type="aff" rid="aff1">'
            '<sup>1</sup>'
            '</xref>'
            '</contrib>'
            '</contrib-group>'
            '<aff id="aff1">'
            '<institution content-type="original">Universidade Federal do Rio Grande do Sul, Escola de Enfermagem, Programa de Pós-Graduação em Enfermagem, Porto Alegre, RS, Brazil.</institution>'
            '<institution content-type="orgname">Universidade Federal do Rio Grande do Sul</institution>'
            '<institution content-type="orgdiv1">Escola de Enfermagem</institution>'
            '<institution content-type="orgdiv2">Programa de Pós-Graduação em Enfermagem</institution>'
            '<addr-line>'
            '<named-content content-type="city">Porto Alegre</named-content>'
            '<named-content content-type="state">RS</named-content>'
            '</addr-line>'
            '<country country="BR">Brazil</country>'
            '</aff>'
            '</article-meta>'
            '</front>'
            '</article>'
        )

        xml_pmc_aff(xml_tree)

        obtained = ET.tostring(xml_tree, encoding="utf-8").decode("utf-8")

        self.assertEqual(obtained, expected)

    def test_xml_pmc_ref(self):
        self.maxDiff = None
        expected = (
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<back>'
            '<ref-list>'
            '<title>REFERENCES</title>'
            '<ref id="B1">'
            '<label>1.</label>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Tran</surname>'
            '<given-names>B</given-names>'
            '</name>'
            '<name>'
            '<surname>Falster</surname>'
            '<given-names>MO</given-names>'
            '</name>'
            '<name>'
            '<surname>Douglas</surname>'
            '<given-names>K</given-names>'
            '</name>'
            '<name>'
            '<surname>Blyth</surname>'
            '<given-names>F</given-names>'
            '</name>'
            '<name>'
            '<surname>Jorm</surname>'
            '<given-names>LR</given-names>'
            '</name>'
            '</person-group>'
            '<article-title>Smoking and potentially preventable hospitalisation: the benefit of smoking cessation in older ages</article-title>'
            '<source>Drug Alcohol Depend.</source>'
            '<year>2015</year>'
            '<volume>150</volume>'
            '<fpage>85</fpage>'
            '<lpage>91</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.1016/j.drugalcdep.2015.02.028">https://doi.org/10.1016/j.drugalcdep.2015.02.028</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '<ref id="B2">'
            '<label>2.</label>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Kwon</surname>'
            '<given-names>JA</given-names>'
            '</name>'
            '<name>'
            '<surname>Jeon</surname>'
            '<given-names>W</given-names>'
            '</name>'
            '<name>'
            '<surname>Park</surname>'
            '<given-names>EC</given-names>'
            '</name>'
            '<name>'
            '<surname>Kim</surname>'
            '<given-names>JH</given-names>'
            '</name>'
            '<name>'
            '<surname>Kim</surname>'
            '<given-names>SJ</given-names>'
            '</name>'
            '<name>'
            '<surname>Yoo</surname>'
            '<given-names>KB</given-names>'
            '</name>'
            '<etal/>'
            '</person-group>'
            '<article-title>Effects of disease detection on changes in smoking behavior</article-title>'
            '<source>Yonsei Med J.</source>'
            '<year>2015</year>'
            '<volume>56</volume>'
            '<issue>4</issue>'
            '<fpage>1143</fpage>'
            '<lpage>9</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.3349/ymj.2015.56.4.1143">https://doi.org/10.3349/ymj.2015.56.4.1143</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '<ref id="B3">'
            '<label>3.</label>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Vogiatzis</surname>'
            '<given-names>I</given-names>'
            '</name>'
            '<name>'
            '<surname>Pantzartzidou</surname>'
            '<given-names>A</given-names>'
            '</name>'
            '<name>'
            '<surname>Pittas</surname>'
            '<given-names>S</given-names>'
            '</name>'
            '<name>'
            '<surname>Papavasiliou</surname>'
            '<given-names>E</given-names>'
            '</name>'
            '</person-group>'
            '<article-title>Smoking cessation advisory intervention in patients with cardiovascular disease</article-title>'
            '<source>Med Arch.</source>'
            '<year>2017</year>'
            '<volume>71</volume>'
            '<issue>2</issue>'
            '<fpage>128</fpage>'
            '<lpage>31</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131">https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '</ref-list>'
            '</back>'
            '</article>'

        )
        xml_tree = ET.fromstring(
            '<article xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" dtd-version="1.1" specific-use="sps-1.9" xml:lang="en">'
            '<back>'
            '<ref-list>'
            '<title>REFERENCES</title>'
            '<ref id="B1">'
            '<label>1.</label>'
            '<mixed-citation>'
            '1. Tran B, Falster MO, Douglas K, Blyth F, Jorm LR. Smoking and potentially preventable hospitalisation: the benefit of smoking cessation in older ages. Drug Alcohol Depend. 2015;150:85-91. DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.1016/j.drugalcdep.2015.02.028">https://doi.org/10.1016/j.drugalcdep.2015.02.028</ext-link>'
            '</mixed-citation>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Tran</surname>'
            '<given-names>B</given-names>'
            '</name>'
            '<name>'
            '<surname>Falster</surname>'
            '<given-names>MO</given-names>'
            '</name>'
            '<name>'
            '<surname>Douglas</surname>'
            '<given-names>K</given-names>'
            '</name>'
            '<name>'
            '<surname>Blyth</surname>'
            '<given-names>F</given-names>'
            '</name>'
            '<name>'
            '<surname>Jorm</surname>'
            '<given-names>LR</given-names>'
            '</name>'
            '</person-group>'
            '<article-title>Smoking and potentially preventable hospitalisation: the benefit of smoking cessation in older ages</article-title>'
            '<source>Drug Alcohol Depend.</source>'
            '<year>2015</year>'
            '<volume>150</volume>'
            '<fpage>85</fpage>'
            '<lpage>91</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.1016/j.drugalcdep.2015.02.028">https://doi.org/10.1016/j.drugalcdep.2015.02.028</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '<ref id="B2">'
            '<label>2.</label>'
            '<mixed-citation>'
            '2. Kwon JA, Jeon W, Park EC, Kim JH, Kim SJ, Yoo KB, et al. Effects of disease detection on changes in smoking behavior. Yonsei Med J. 2015;56(4): 1143-9. DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.3349/ymj.2015.56.4.1143">https://doi.org/10.3349/ymj.2015.56.4.1143</ext-link>'
            '</mixed-citation>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Kwon</surname>'
            '<given-names>JA</given-names>'
            '</name>'
            '<name>'
            '<surname>Jeon</surname>'
            '<given-names>W</given-names>'
            '</name>'
            '<name>'
            '<surname>Park</surname>'
            '<given-names>EC</given-names>'
            '</name>'
            '<name>'
            '<surname>Kim</surname>'
            '<given-names>JH</given-names>'
            '</name>'
            '<name>'
            '<surname>Kim</surname>'
            '<given-names>SJ</given-names>'
            '</name>'
            '<name>'
            '<surname>Yoo</surname>'
            '<given-names>KB</given-names>'
            '</name>'
            '<etal/>'
            '</person-group>'
            '<article-title>Effects of disease detection on changes in smoking behavior</article-title>'
            '<source>Yonsei Med J.</source>'
            '<year>2015</year>'
            '<volume>56</volume>'
            '<issue>4</issue>'
            '<fpage>1143</fpage>'
            '<lpage>9</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://doi.org/10.3349/ymj.2015.56.4.1143">https://doi.org/10.3349/ymj.2015.56.4.1143</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '<ref id="B3">'
            '<label>3.</label>'
            '<mixed-citation>'
            '3. Vogiatzis I, Pantzartzidou A, Pittas S, Papavasiliou E. Smoking cessation advisory intervention in patients with cardiovascular disease. Med Arch. 2017;71(2):128-31. DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131">https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131</ext-link>'
            '</mixed-citation>'
            '<element-citation publication-type="journal">'
            '<person-group person-group-type="author">'
            '<name>'
            '<surname>Vogiatzis</surname>'
            '<given-names>I</given-names>'
            '</name>'
            '<name>'
            '<surname>Pantzartzidou</surname>'
            '<given-names>A</given-names>'
            '</name>'
            '<name>'
            '<surname>Pittas</surname>'
            '<given-names>S</given-names>'
            '</name>'
            '<name>'
            '<surname>Papavasiliou</surname>'
            '<given-names>E</given-names>'
            '</name>'
            '</person-group>'
            '<article-title>Smoking cessation advisory intervention in patients with cardiovascular disease</article-title>'
            '<source>Med Arch.</source>'
            '<year>2017</year>'
            '<volume>71</volume>'
            '<issue>2</issue>'
            '<fpage>128</fpage>'
            '<lpage>31</lpage>'
            '<comment>'
            'DOI:'
            '<ext-link ext-link-type="uri" xlink:href="https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131">https://dx.doi.org/10.5455%2Fmedarh.2017.71.128-131</ext-link>'
            '</comment>'
            '</element-citation>'
            '</ref>'
            '</ref-list>'
            '</back>'
            '</article>'
        )

        xml_pmc_ref(xml_tree)

        obtained = ET.tostring(xml_tree, encoding="utf-8").decode("utf-8")

        self.assertEqual(obtained, expected)


if __name__ == '__main__':
    unittest.main()
