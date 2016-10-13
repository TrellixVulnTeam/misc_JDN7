import logging
from collections import Counter
import xml.sax

DMOZ_FILE = "content.rdf.u8.gz"
DMOZ_URL = "http://rdf.dmoz.org/rdf/content.rdf.u8.gz"
DMOZ_JSON = "dmoz.json"
# CATEGORIES = list(set(["Arts", "Business", "Computers", "Health"]))
CATEGORIES = []
CAT_PREFIX = "Top/"


class DmozHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self._current_page = ''
        self._capture_content = False
        self._current_content = {}
        self._expect_end = False
        self.count = []
        self.dmoz = {}
        for cat in CATEGORIES:
            self.dmoz.setdefault(cat, [])

    def startElement(self, name, attrs):
        if name == 'ExternalPage':
            self._current_page = attrs['about']
            self._current_content = {}
        elif name in ['d:Title', 'd:Description', 'priority', 'topic']:
            self._capture_content = True
            self._capture_content_type = name

    def endElement(self, name):
        # Make sure that the only thing after "topic" is "/ExternalPage"
        if self._expect_end:
            assert name == 'topic' or name == 'ExternalPage'
            if name == 'ExternalPage':
                self._expect_end = False

    def characters(self, content):
        if self._capture_content:
            assert not self._expect_end
            self._current_content[self._capture_content_type] = content
            # logging.info self._capture_content_type, self._current_content[self._capture_content_type]

            # This makes the assumption that "topic" is the last entity in each dmoz page:
            if self._capture_content_type == "topic":
                # add url to self.dmoz
                if content and content.startswith(CAT_PREFIX):
                    top_cat = content.split('/')[1]
                    if top_cat:
                        self.count.append(top_cat)
                    cat = content[len(CAT_PREFIX):]
                    for i in range(len(CATEGORIES)):
                        if cat.startswith(CATEGORIES[i]):
                            m_id = len(self.dmoz[CATEGORIES[i]])
                            title = self._current_content.get("d:Title", "")
                            desc = self._current_content.get("d:Description",
                                                             "")
                            self.dmoz[CATEGORIES[i]].append(
                                {"id": m_id,
                                 "url": self._current_page,
                                 "title": title,
                                 "desc": desc})
                            # logging.info("url:"+ self._current_page)
                self._expect_end = True
            self._capture_content = False


def parse_dmoz(file_path):
    """parse dmoz xml content file.
    args:
        file_path (str): path of dmoz file.
    return:
        dmoz (dict): categories map to web pages.
        count (Counter): # of url in every categories.
    """
    logging.info("parsing dmoz xml file... (it may take several minites)")
    # create an XMLReader
    parser = xml.sax.make_parser()
    handler = DmozHandler()
    parser.setContentHandler(handler)
    parser.parse(file_path)

    logging.info("dmoz:{}".format({k: len(handler.dmoz[k])
                                   for k in handler.dmoz.keys()}))
    logging.info("count:{}".format(Counter(handler.count)))
    logging.info("parsed dmoz xml successfully")
    # write_json(dmoz_json, handler.dmoz)

def set_logging(level=logging.INFO, stream=False, fileh=False, filename="example.log"):
    """set basic logging configurations (root logger).
    args:
        stream (bool): whether print log to console.
        fileh (bool): whether write log to file.
        filename (str): the path of log file.
    return:
        configued root logger.
    """
    handlers = []
    level = level
    log_format = '%(asctime)s: %(message)s'

    if stream:
        handlers.append(logging.StreamHandler())
    if fileh:
        handlers.append(logging.FileHandler(filename))
    logging.basicConfig(format=log_format, handlers=handlers, level=level)
    return logging.getLogger()


set_logging(level=20, stream=True)
dmoz_file = "/Users/yuhuilin/Downloads/wpc/content.rdf.u8/content.rdf.u8"
parse_dmoz(dmoz_file)
