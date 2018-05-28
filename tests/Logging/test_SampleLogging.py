import os

from thug.Logging.SampleLogging import SampleLogging

sample_logging = SampleLogging()


class TestSampleLogging:
    pe_path  = os.path.join(os.getcwd(), "tests/test_files/sample.exe")
    pdf_path = os.path.join(os.getcwd(), "tests/test_files/sample.pdf")
    jar_path = os.path.join(os.getcwd(), "tests/test_files/sample.jar")
    swf_path = os.path.join(os.getcwd(), "tests/test_files/sample.swf")
    doc_path = os.path.join(os.getcwd(), "tests/test_files/sample.doc")
    rtf_path = os.path.join(os.getcwd(), "tests/test_files/sample.rtf")

    def test_get_none(self):
        assert not sample_logging.get_sample_type("")

    def test_get_pe(self):
        file_type = sample_logging.get_sample_type(open(self.pe_path).read())
        assert file_type in ('PE', )

    def test_get_pdf(self):
        file_type = sample_logging.get_sample_type(open(self.pdf_path).read(1024))
        assert file_type in ('PDF', )

    def test_get_jar(self):
        file_type = sample_logging.get_sample_type(open(self.jar_path).read())
        assert file_type in ('JAR', )

    def test_get_swf(self):
        file_type = sample_logging.get_sample_type(open(self.swf_path).read())
        assert file_type in ('SWF', )

    def test_get_doc(self):
        file_type = sample_logging.get_sample_type(open(self.doc_path).read())
        assert file_type in ('DOC', )

    def test_get_rtf(self):
        file_type = sample_logging.get_sample_type(open(self.rtf_path).read())
        assert file_type in ('RTF', )

    def test_get_imphash(self):
        imphash = sample_logging.get_imphash(open(self.pe_path).read())
        assert imphash in ('5ef204cfbc53779500a050c36dea14fc', )

        imphash = sample_logging.get_imphash(open(self.doc_path).read())
        assert not imphash

    def test_build_sample(self):
        data  = open(self.pe_path).read()
        build = sample_logging.build_sample(data = data, url = self.pe_path, sampletype = 'PE')
        assert build

        build = sample_logging.build_sample(data = data, url = self.pe_path)
        assert build

        build = sample_logging.build_sample(data = "")
        assert not build

        build = sample_logging.build_sample(data = "not_valid")
        assert not build
