import unittest
import xml.etree.ElementTree as ET
from packtools.sps.formats.sps_xml.disp_formula import build_disp_formula



class TestBuildDispFormulaId(unittest.TestCase):
    def test_build_disp_formula_id(self):
        data = {
            "formula-id": "e01",
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": "fórmula no formato mml"
                }
            ]
        }
        expected_xml_str = (
            '<disp-formula id="e01">'
            '<mml:math id="m1">fórmula no formato mml</mml:math>'
            '</disp-formula>'
        )
        disp_formula_elem = build_disp_formula(data)
        generated_xml_str = ET.tostring(disp_formula_elem, encoding="unicode", method="xml")
        self.assertEqual(generated_xml_str.strip(), expected_xml_str.strip())

    def test_build_disp_formula_id_None(self):
        data = {
            "formula-id": None,
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": "fórmula no formato mml"
                }
            ]
        }
        with self.assertRaises(ValueError) as e:
            build_disp_formula(data)
        self.assertEqual(str(e.exception), "formula-id is required")


class TestBuildDispFormulaLabel(unittest.TestCase):
    def test_build_disp_formula_label(self):
        data = {
            "formula-id": "e01",
            "label": "(1)",
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": "fórmula no formato mml"
                }
            ]
        }
        expected_xml_str = (
            '<disp-formula id="e01">'
            '<label>(1)</label>'
            '<mml:math id="m1">fórmula no formato mml</mml:math>'
            '</disp-formula>'
        )
        disp_formula_elem = build_disp_formula(data)
        generated_xml_str = ET.tostring(disp_formula_elem, encoding="unicode", method="xml")
        self.assertEqual(generated_xml_str.strip(), expected_xml_str.strip())

    def test_build_disp_formula_label_None(self):
        data = {
            "formula-id": "e01",
            "label": None,
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": "fórmula no formato mml"
                }
            ]
        }
        expected_xml_str = (
            '<disp-formula id="e01">'
            '<mml:math id="m1">fórmula no formato mml</mml:math>'
            '</disp-formula>'
        )
        disp_formula_elem = build_disp_formula(data)
        generated_xml_str = ET.tostring(disp_formula_elem, encoding="unicode", method="xml")
        self.assertEqual(generated_xml_str.strip(), expected_xml_str.strip())


class TestBuildDispFormula(unittest.TestCase):
    def test_build_disp_formula_codification_None(self):
        data = {
            "formula-id": "e01",
            "label": "(1)",
            "formulas": None
        }
        with self.assertRaises(ValueError) as e:
            build_disp_formula(data)
        self.assertEqual(str(e.exception), "At least one representation of the formula is required")

    def test_build_disp_formula_codification_id_None(self):
        data = {
            "formula-id": "e01",
            "label": "(1)",
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": None,
                    "text": "fórmula no formato mml"
                }
            ]
        }
        with self.assertRaises(ValueError) as e:
            build_disp_formula(data)
        self.assertEqual(str(e.exception), "Missing required fields: id")

    def test_build_disp_formula_formula_None(self):
        data = {
            "formula-id": "e01",
            "label": "(1)",
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": None
                }
            ]
        }
        with self.assertRaises(ValueError) as e:
            build_disp_formula(data)
        self.assertEqual(str(e.exception), "Missing required fields: text")


class TestBuildDispFormulaAlternatives(unittest.TestCase):
    def test_build_disp_formula_alternatives(self):
        data = {
            "formula-id": "e01",
            "label": "(1)",
            "formulas": [
                {
                    "codification": "mml:math",
                    "id": "m1",
                    "text": "fórmula no formato mml"
                },
                {
                    "codification": "tex-math",
                    "id": "t1",
                    "text": "fórmula no formato tex"
                },
                {
                    "codification": "graphic",
                    "id": "g1",
                    "text": "0103-507X-rbti-26-02-0089-ee10.svg"
                }
            ]
        }
        expected_xml_str = (
            '<disp-formula id="e01">'
            '<label>(1)</label>'
            '<alternatives>'
            '<mml:math id="m1">fórmula no formato mml</mml:math>'
            '<tex-math id="t1">fórmula no formato tex</tex-math>'
            '<graphic xlink:href="0103-507X-rbti-26-02-0089-ee10.svg" id="g1" />'
            '</alternatives>'
            '</disp-formula>'
        )
        disp_formula_elem = build_disp_formula(data)
        generated_xml_str = ET.tostring(disp_formula_elem, encoding="unicode", method="xml")
        self.assertEqual(generated_xml_str.strip(), expected_xml_str.strip())