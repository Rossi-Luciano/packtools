from unittest import TestCase
from lxml import etree

from packtools.sps.validation.front_articlemeta_issue import (
    IssueValidation,
    PaginationValidation,
)


class IssueTest(TestCase):
    def setUp(self):

        self.expected_keys = ["title", "parent", "parent_article_type", "parent_id", "parent_lang", "response", "item", "sub_item",
                "validation_type", "expected_value", "got_value", "advice", "message", "data"]

        self.params = {
            "volume_format_error_level": "CRITICAL",
            "number_format_error_level": "CRITICAL",
            "supplement_format_error_level": "CRITICAL",
            "issue_format_error_level": "CRITICAL",
            "expected_issues_error_level": "CRITICAL",
            "pagination_error_level": "CRITICAL",
            "journal_data": {
                "issues": [{"volume": "56", "number": "3", "supplement": "1"}]
            },
        }

    def test_volume_matches(self):
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_volume_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "issue volume format")
        self.assertEqual(obtained["response"], "OK")
        self.assertEqual(obtained["message"], "Got 56, expected 56")
        self.assertIsNone(obtained["advice"])

    def test_volume_no_matches(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume> 56 </volume>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_volume_format()

        self.assertEqual(obtained["title"], "issue volume format")
        self.assertEqual(obtained["response"], "CRITICAL")
        self.assertEqual(obtained["message"], "Got  56 , expected alphanumeric value")
        self.assertEqual(obtained["advice"], "Replace  56  in <article-meta><volume> with alphanumeric value")

    def test_volume_there_is_tag_there_is_no_value(self):
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume></volume>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_volume_format()

        self.assertIsNone(obtained)

    def test_volume_there_is_no_tag_there_is_no_value(self):
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_volume_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue_without_value(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue_out_of_pattern_value(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <issue>vol 4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "issue number format")
        self.assertEqual(obtained["response"], "OK")
        self.assertEqual(obtained["message"], "Got vol4, expected vol4")
        self.assertIsNone(obtained["advice"])

    def test_validate_article_issue_number_success(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "issue number format")
        self.assertEqual(obtained["response"], "OK")
        self.assertEqual(obtained["message"], "Got 4, expected 4")
        self.assertIsNone(obtained["advice"])

    def test_validate_article_issue_number_there_is_tag_there_is_no_value(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue></issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue_number_there_is_no_tag_there_is_no_value(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue_number_start_with_zero(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>04</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "number",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "ERROR",
            "item": "number",
            "sub_item": None,
            "validation_type": "format",
            "expected_value": "4",
            "got_value": "04",
            "message": "Got 04, expected 4",
            "advice": "Consulte SPS documentation to complete issue element",
            "data": {"number": "04", "volume": "56"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "issue number format")
        self.assertEqual(obtained["response"], "CRITICAL")
        self.assertEqual(obtained["message"], "Got 04, expected 4")
        self.assertEqual(obtained["advice"], "Replace 04 in <article-meta><issue> with 4")

    def test_validate_article_issue_number_value_is_not_numeric(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4a</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "number",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "number",
            "sub_item": None,
            "validation_type": "format",
            "expected_value": "4a",
            "got_value": "4a",
            "message": "Got 4a, expected 4a",
            "advice": None,
            "data": {"number": "4a", "volume": "56"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_number_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "issue number format")
        self.assertEqual(obtained["response"], "OK")
        self.assertEqual(obtained["message"], "Got 4a, expected 4a")
        self.assertIsNone(obtained["advice"])

    def test_validate_article_issue_special_number(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>spa 1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "special or supplement")
        self.assertEqual(obtained["response"], "CRITICAL")
        self.assertEqual(obtained["message"], "Got {'type_value': '1', 'type': 'spa', 'type_valid_format': False}, expected ['suppl 1', 'spe 1']")
        self.assertEqual(obtained["advice"], "Replace spa 1 in <article-meta><issue> with one of ['suppl 1', 'spe 1']")

    def test_validate_article_issue_special_number_with_dot(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>spe.1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue_special_number_with_space(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue> spe 1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["spe 1"],
            "got_value": {"type": "spe", "type_valid_format": True, "type_value": "1"},
            "message": "Got {'type_value': '1', 'type': 'spe', 'type_valid_format': True}, expected ['spe 1']",
            "advice": None,
            "data": {"issue": " spe 1"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_validate_article_issue_supplement(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>suppl 1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["suppl 1"],
            "got_value": {
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "1",
            },
            "message": "Got {'type_value': '1', 'type': 'suppl', 'type_valid_format': True}, expected ['suppl 1']",
            "advice": None,
            "data": {"issue": "suppl 1"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_validate_article_issue_supplement_with_dot(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>suppl a.</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["suppl a."],
            "got_value": {
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "a.",
            },
            "message": "Got {'type_value': 'a.', 'type': 'suppl', 'type_valid_format': True}, expected ['suppl a.']",
            "advice": None,
            "data": {"issue": "suppl a."},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_validate_article_issue_supplement_number_starts_with_zero(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>suppl 04</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["suppl 04"],
            "got_value": {
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "04",
            },
            "message": "Got {'type_value': '04', 'type': 'suppl', 'type_valid_format': True}, expected ['suppl 04']",
            "advice": None,
            "data": {"issue": "suppl 04"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_validate_article_issue_number_supplement(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4 suppl 1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["4 suppl 1"],
            "got_value": {
                "number": "4",
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "1",
            },
            "message": "Got {'number': '4', 'type_value': '1', 'type': 'suppl', 'type_valid_format': True}, expected ['4 suppl 1']",
            "advice": None,
            "data": {"issue": "4 suppl 1"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_validate_article_issue_number_supplement_with_dot_and_space(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue> a suppl b.</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["a suppl b."],
            "got_value": {
                "number": "a",
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "b.",
            },
            "message": "Got {'number': 'a', 'type_value': 'b.', 'type': 'suppl', 'type_valid_format': True}, expected ['a suppl b.']",
            "advice": None,
            "data": {"issue": " a suppl b."},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_suppl_matches(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4</issue>
                        <supplement>*2</supplement>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "supplement format",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "CRITICAL",
            "item": "supplement",
            "sub_item": None,
            "validation_type": "format",
            "expected_value": "alphanumeric value",
            "got_value": "*2",
            "message": "Got *2, expected alphanumeric value",
            "advice": "Replace *2 in <article-meta><supplement> with alphanumeric value",
            "data": {"number": "4", "suppl": "*2", "volume": "56"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_supplement_format()

        self.assertDictEqual(expected, obtained)

    def test_suppl_no_matches(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4</issue>
                        <supplement>2b</supplement>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "supplement format",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "supplement",
            "sub_item": None,
            "validation_type": "format",
            "expected_value": "2b",
            "got_value": "2b",
            "message": "Got 2b, expected 2b",
            "advice": None,
            "data": {"number": "4", "suppl": "2b", "volume": "56"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_supplement_format()

        self.assertDictEqual(expected, obtained)

    def test_suppl_implicit(self):
        self.maxDiff = None  # Permite exibir diferenças detalhadas em caso de falha
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4 suppl 2</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        expected = {
            "title": "special or supplement",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "response": "OK",
            "item": "issue",
            "sub_item": "special or supplement",
            "validation_type": "format",
            "expected_value": ["4 suppl 2"],
            "got_value": {
                "number": "4",
                "type": "suppl",
                "type_valid_format": True,
                "type_value": "2",
            },
            "message": "Got {'number': '4', 'type_value': '2', 'type': 'suppl', 'type_valid_format': True}, expected ['4 suppl 2']",
            "advice": None,
            "data": {"issue": "4 suppl 2"},
        }

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_issue_format()

        self.assertDictEqual(expected, obtained)

    def test_suppl_without_suppl(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4</issue>
                    </article-meta>
                </front>
            </article>
            """
        )

        validator = IssueValidation(
            xml_tree, params=self.params
        )

        obtained = validator.validate_supplement_format()

        self.assertIsNone(obtained)

    def test_validate_article_issue(self):
        self.maxDiff = None
        xml_tree = etree.fromstring(
            """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                        <issue>4 suppl 1</issue>
                    </article-meta>
                </front>
            </article>
            """
        )


        validator = IssueValidation(
            xml_tree,
            params=self.params,
        )

        obtained = list(validator.validate())

        self.assertEqual(len(obtained), 5)
        for i, item in enumerate(obtained):
            for key in self.expected_keys:
                with self.subTest(f"item: {i}, key: {key}"):
                    self.assertIn(key, item, f"{key} not found")


class PaginationTest(TestCase):
    def setUp(self):

        self.expected_keys = ["title", "parent", "parent_article_type", "parent_id", "parent_lang", "response", "item", "sub_item",
                "validation_type", "expected_value", "got_value", "advice", "message", "data"]

        self.params = {
            "volume_format_error_level": "CRITICAL",
            "number_format_error_level": "CRITICAL",
            "supplement_format_error_level": "CRITICAL",
            "issue_format_error_level": "CRITICAL",
            "expected_issues_error_level": "CRITICAL",
            "pagination_error_level": "CRITICAL",
            "journal_data": {
                "issues": [{"volume": "56", "number": "4", "supplement": "1"}]
            },
        }

    def test_validation_pages(self):
        self.maxDiff = None
        xml = """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                    </article-meta>
                </front>
            </article>
            """
        xml_tree = etree.fromstring(xml)

        expected = {
            "title": "Pagination",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "item": "elocation-id | fpage / lpage",
            "sub_item": "elocation-id | fpage / lpage",
            "validation_type": "match",
            "response": "CRITICAL",
            "expected_value": "elocation-id or fpage + lpage",
            "got_value": "elocation-id: None, fpage: None, lpage: None",
            "message": "Got elocation-id: None, fpage: None, lpage: None, expected elocation-id or fpage + lpage",
            "advice": "Provide elocation-id or fpage + lpage",
            "data": {"volume": "56"},
        }

        obtained = PaginationValidation(xml_tree, self.params).validate()

        self.assertDictEqual(expected, obtained)

    def test_validation_e_location(self):
        self.maxDiff = None
        xml = """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <volume>56</volume>
                    </article-meta>
                </front>
            </article>
            """
        xml_tree = etree.fromstring(xml)

        expected = {
            "title": "Pagination",
            "parent": "article",
            "parent_article_type": None,
            "parent_id": None,
            "parent_lang": None,
            "item": "elocation-id | fpage / lpage",
            "sub_item": "elocation-id | fpage / lpage",
            "validation_type": "match",
            "response": "CRITICAL",
            "expected_value": "elocation-id or fpage + lpage",
            "got_value": "elocation-id: None, fpage: None, lpage: None",
            "message": "Got elocation-id: None, fpage: None, lpage: None, expected elocation-id or fpage + lpage",
            "advice": "Provide elocation-id or fpage + lpage",
            "data": {"volume": "56"},
        }

        obtained = PaginationValidation(xml_tree, self.params).validate()

        self.assertDictEqual(expected, obtained)

    def test_validation_pages_and_e_location_exists_fail(self):
        self.maxDiff = None
        xml = """
            <article xmlns:xlink="http://www.w3.org/1999/xlink" article-type="research-article" xml:lang="en">
                <front>
                    <article-meta>
                        <elocation-id>e51467</elocation-id>
                        <fpage>220</fpage>
                        <lpage>240</lpage>
                    </article-meta>
                </front>
            </article>
            """

        xml_tree = etree.fromstring(xml)

        obtained = PaginationValidation(xml_tree, self.params).validate()

        for key in self.expected_keys:
            self.assertIn(key, obtained, f"{key} not found")

        self.assertEqual(obtained["title"], "Pagination")
        self.assertEqual(obtained["response"], "OK")
        self.assertEqual(obtained["message"], "Got elocation-id: e51467, fpage: 220, lpage: 240, expected elocation-id or fpage + lpage")
        self.assertIsNone(obtained["advice"])
