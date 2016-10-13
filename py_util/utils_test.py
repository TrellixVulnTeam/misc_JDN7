from utils import CUR_TIME
from utils import logger
from utils import FLAGS

# ================================
# test logging
# ================================
# utils.set_logging(stream=False)
# utils.set_logger(stream=True)
# logger.info("logger111111")
logger.set_logger(stream=True)
logger.info(CUR_TIME)
logger.newline()
logger.error("newline beneath~")
logger.newline(2)
logger.info("haha")

# ================================
# test FLAGS
# ================================
FLAGS.add("--aa", type=float, default=11., help="doc for dd")
logger.info("aa: {}".format(FLAGS.get('aa')))
# for flag that should be overwrite later, don't set default
FLAGS.add("--bb", type=int, default=None, help="doc for dd")
if FLAGS.get('aa') == 11:
    FLAGS.overwrite_none(bb=15)

FLAGS.add("--cc", type=bool, default=False, help="doc for dd")
FLAGS.add("--dd", type=str, default="dddddd", help="doc for dd")
# for flag that should be overwrite later, don't set default
FLAGS.add("--ff", type=str, help="doc for dd")
FLAGS.add("--gg", type=str, help="doc for dd")
FLAGS.add("--hh", type=str, default="hhhhh", help="doc for dd")
# overwrite or set new default values
FLAGS.overwrite_defaults(dd="replaced dd", ee="an extra flag", ff="ff")
FLAGS.overwrite_none(hh="this won't show", gg="gggg", ii="illigal")
FLAGS.add("--jj", type=str, default="hhhhh", help="doc for dd")

# parse FLAGS at the start of main()
FLAGS.parse_and_log()
logger.info(FLAGS.gg)
logger.info(FLAGS.ii)
