import unittest
from lxml import etree

from packtools.sps.validation.article_data_availability import DataAvailabilityValidation


class DataAvailabilityTest(unittest.TestCase):

    def test_validate_data_availability_fn_ok(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" 
                dtd-version="1.0" article-type="research-article" xml:lang="pt">
                    <back>
                        <fn-group>
                            <fn fn-type="data-availability" specific-use="data-available" id="fn1">
                                <label>Data Availability Statement</label>
                                <p>The data and code used to generate plots and perform statistical analyses have been
                                uploaded to the Open Science Framework archive: <ext-link ext-link-type="uri"
                                xlink:href="https://osf.io/jw6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e">https://osf.io/j
                                w6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e</ext-link>.</p>
                            </fn>
                        </fn-group>
                    </back>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'article',
                'parent_article_type': 'research-article',
                'parent_id': None,
                'parent_lang': "pt",
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'OK',
                'expected_value': "data-available",
                'got_value': 'data-available',
                'message': "Got data-available, expected one of ['data-available', 'data-available-upon-request']",
                'advice': None,
                'data': {
                    'parent': 'article',
                    'parent_article_type': 'research-article',
                    'parent_id': None,
                    'parent_lang': "pt",
                    'specific_use': 'data-available',
                    'tag': 'fn'
                },
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-available", "data-available-upon-request"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)

    def test_validate_data_availability_sec_ok(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" 
                dtd-version="1.0" article-type="research-article" xml:lang="pt">
                    <back>
                        <sec sec-type="data-availability" specific-use="data-available-upon-request">
                            <label>Data availability statement</label>
                            <p>Data will be available upon request.</p>
                        </sec>
                    </back>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'article',
                'parent_article_type': 'research-article',
                'parent_id': None,
                'parent_lang': "pt",
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'OK',
                'expected_value': "data-available-upon-request",
                'got_value': 'data-available-upon-request',
                'message': "Got data-available-upon-request, expected one of ['data-available', 'data-available-upon-request']",
                'advice': None,
                'data': {
                    'parent': 'article',
                    'parent_article_type': 'research-article',
                    'parent_id': None,
                    'parent_lang': "pt",
                    'specific_use': 'data-available-upon-request',
                    'tag': 'sec'
                },
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-available", "data-available-upon-request"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)

    def test_validate_data_availability_fn_not_ok(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" 
                dtd-version="1.0" article-type="research-article" xml:lang="pt">
                    <back>
                        <fn-group>
                            <fn fn-type="data-availability" specific-use="data-available" id="fn1">
                                <label>Data Availability Statement</label>
                                <p>The data and code used to generate plots and perform statistical analyses have been
                                uploaded to the Open Science Framework archive: <ext-link ext-link-type="uri"
                                xlink:href="https://osf.io/jw6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e">https://osf.io/j
                                w6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e</ext-link>.</p>
                            </fn>
                        </fn-group>
                    </back>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'article',
                'parent_article_type': 'research-article',
                'parent_id': None,
                'parent_lang': "pt",
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'ERROR',
                'expected_value': "one of ['data-not-available', 'uninformed']",
                'got_value': 'data-available',
                'message': "Got data-available, expected one of ['data-not-available', 'uninformed']",
                'advice': 'Provide a data availability statement from the following list: data-not-available | uninformed',
                'data': {
                    'parent': 'article',
                    'parent_article_type': 'research-article',
                    'parent_id': None,
                    'parent_lang': "pt",
                    'specific_use': 'data-available',
                    'tag': 'fn'
                },
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-not-available", "uninformed"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)

    def test_validate_data_availability_sec_not_ok(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" 
                dtd-version="1.0" article-type="research-article" xml:lang="pt">
                    <back>
                        <sec sec-type="data-availability" specific-use="data-available-upon-request">
                            <label>Data availability statement</label>
                            <p>Data will be available upon request.</p>
                        </sec>
                    </back>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'article',
                'parent_article_type': 'research-article',
                'parent_id': None,
                'parent_lang': "pt",
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'ERROR',
                'expected_value': "one of ['data-not-available', 'uninformed']",
                'got_value': 'data-available-upon-request',
                'message': "Got data-available-upon-request, expected one of ['data-not-available', 'uninformed']",
                'advice': 'Provide a data availability statement from the following list: data-not-available | uninformed',
                'data': {
                    'parent': 'article',
                    'parent_article_type': 'research-article',
                    'parent_id': None,
                    'parent_lang': "pt",
                    'specific_use': 'data-available-upon-request',
                    'tag': 'sec'
                },
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-not-available", "uninformed"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)

    def test_validate_data_availability_without_data_availability(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:mml="http://www.w3.org/1998/Math/MathML" 
                dtd-version="1.0" article-type="research-article" xml:lang="pt">
                    <back>
                    </back>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'article',
                'parent_article_type': 'research-article',
                'parent_id': None,
                'parent_lang': "pt",
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'ERROR',
                'expected_value': "one of ['data-available', 'data-available-upon-request']",
                'got_value': None,
                'message': "Got None, expected one of ['data-available', 'data-available-upon-request']",
                'advice': 'Provide a data availability statement from the following list: data-available | data-available-upon-request',
                'data': None,
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-available", "data-available-upon-request"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)

    def test_validate_data_availability_subarticle_fn_ok(self):
        self.maxDiff = None
        xml = """
                <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article">
                    <sub-article article-type="translation" id="TRen" xml:lang="en">
                        <back>
                            <fn-group>
                                <fn fn-type="data-availability" specific-use="data-available" id="fn1">
                                    <label>Data Availability Statement</label>
                                    <p>The data and code used to generate plots and perform statistical analyses have been
                                    uploaded to the Open Science Framework archive: <ext-link ext-link-type="uri"
                                    xlink:href="https://osf.io/jw6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e">https://osf.io/j
                                    w6vg/?view_only=0335a15b6db3477f93d0ae636cdf3b4e</ext-link>.</p>
                                </fn>
                            </fn-group>
                        </back>
                    </sub-article>
                </article>
            """
        xmltree = etree.fromstring(xml)
        expected = [
            {
                'title': 'Data availability validation',
                'parent': 'sub-article',
                'parent_article_type': 'translation',
                'parent_id': 'TRen',
                'parent_lang': 'en',
                'item': 'fn | sec',
                'sub_item': '@specific-use',
                'validation_type': 'value in list',
                'response': 'OK',
                'expected_value': 'data-available',
                'got_value': 'data-available',
                'message': "Got data-available, expected one of ['data-available', 'data-available-upon-request']",
                'advice': None,
                'data': {
                    'parent': 'sub-article',
                    'parent_article_type': 'translation',
                    'parent_id': 'TRen',
                    'parent_lang': 'en',
                    'specific_use': 'data-available',
                    'tag': 'fn'
                },
            }
        ]
        obtained = list(DataAvailabilityValidation(xmltree).validate_data_availability(
            ["data-available", "data-available-upon-request"]))

        for i, item in enumerate(expected):
            with self.subTest(i):
                self.assertDictEqual(obtained[i], item)


if __name__ == '__main__':
    unittest.main()
