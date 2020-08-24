from pathlib import Path

from django.test import TestCase, Client


TEST_DIR = Path(__file__).parent / Path('test_files')


class XMLConversionTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_convert_empty_document(self):
        with (TEST_DIR / Path('empty.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Root": "",
            })

    def test_convert_addresses(self):
        with (TEST_DIR / Path('addresses.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "Addresses": [
                    {
                        "Address": [
                            {"StreetLine1": "123 Main St."},
                            {"StreetLine2": "Suite 400"},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94103"},
                        ]
                    },
                    {
                        "Address": [
                            {"StreetLine1": "400 Market St."},
                            {"City": "San Francisco"},
                            {"State": "CA"},
                            {"PostCode": "94108"},
                        ]
                    },
                ],
            })


    def test_convert_wrong_format(self):
        with (TEST_DIR / Path('not-xml.txt')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertFormError(
                response,
                'form',
                'file',
                'Invalid file. Please upload a valid XML file.'
            )

    def test_convert_broken_xml(self):
        with (TEST_DIR / Path('broken-xml.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertFormError(
                response,
                'form',
                'file',
                'Invalid file. Please upload a valid XML file.'
            )

    def test_convert_multiple_tags(self):
        with (TEST_DIR / Path('multiple-tags.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "PurchaseOrder": [
                    {
                        "Address": [
                              { "Name": "Ellen Adams" },
                              { "Street": "123 Maple Street" },
                              { "City": "Mill Valley" },
                              { "State": "CA" },
                              { "Zip": "10999" },
                              { "Country": "USA" }
                        ]
                    },
                    { 
                        "DeliveryNotes": "Please leave packages in shed by driveway." 
                    },
                    { 
                        "Item": [
                            { "ProductName": "Lawnmower" },
                            { "Quantity": "1" },
                            { "USPrice": "148.95" },
                            { "Comment": "Confirm this is electric" }
                        ]
                    }
                  ]
                })

    def test_convert_ignore_attributes(self):
        with (TEST_DIR / Path('ignore-attributes.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "PurchaseOrder": [
                    {
                        "Address": [
                              { "Name": "Ellen Adams" },
                              { "Street": "123 Maple Street" },
                              { "City": "Mill Valley" },
                              { "State": "CA" },
                              { "Zip": "10999" },
                              { "Country": "USA" }
                        ]
                    },
                    { 
                        "DeliveryNotes": "Please leave packages in shed by driveway." 
                    },
                    { 
                        "Item": [
                            { "ProductName": "Lawnmower" },
                            { "Quantity": "1" },
                            { "USPrice": "148.95" },
                            { "Comment": "Confirm this is electric" }
                        ]
                    }
                  ]
                })

    def test_convert_deep_nesting(self):
        with (TEST_DIR / Path('deep-nesting.xml')).open() as fp:
            response = self.client.post('/', {
                'file': fp,
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {
                "PurchaseOrder": [
                    {
                        "Address": [
                              { "Name": "Ellen Adams" },
                              { "Street": "123 Maple Street" },
                              { "City": "Mill Valley" },
                              { "State": "CA" },
                              { "Zip": "10999" },
                              { "Country": "USA" }
                        ]
                    },
                    { 
                        "DeliveryNotes": "Please leave packages in shed by driveway." 
                    },
                    { 
                        "Items": [
                            {
                                "Item": [
                                    { 
                                        "Product": [
                                            { "Name": "Lawnmower" },
                                            { "Description": "The lawnmower everyone deserves!" }
                                        ] 
                                    },
                                    { "Quantity": "1" },
                                    { "USPrice": "148.95" },
                                    { "Comment": "Confirm this is electric" }
                                ]
                            },
                            {
                                "Item": [
                                    { 
                                        "Product": [
                                            { "Name": "Baby Monitor" },
                                            { "Description": "Keep track of your baby with this baby monitor." }
                                        ] 
                                    },
                                    { "Quantity": "2" },
                                    { "USPrice": "39.98" },
                                    { "ShipDate": "1999-05-21" }
                                ]
                            }
                        ]
                    }
                  ]
                })