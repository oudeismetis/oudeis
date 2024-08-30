+++
title = "Python Exception Suggested Fix"
projectslug = 'foo'
date = "2021-04-23"
categories = [ "thoughts" ]
image = "img/foo.jpeg"
showonlyimage = false
draft = true
+++

"Start with why"
<!--more-->

"python log suggest based on error message"

"python log error suggestion"

https://stackoverflow.com/questions/7274732/extending-the-python-logger

https://docs.python.org/3/howto/logging-cookbook.html#customizing-logrecord

{{< highlight python "linenos=table" >}}
class CustomJsonFormatter(jsonlogger.JsonFormatter):
  def __init__(self, *args, **kwargs):
    self.utility = kwargs.pop('utility_name', None)
    super().__init__(*args, **kwargs)

  def add_fields(self, log_record, record, message_dict):
    super().add_fields(log_record, record, message_dict)
    log_record['timestamp'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    log_record['utility'] = self.utility
    log_record['code_location'] = f'{log_record["module"]}.{log_record["funcName"]}() Line:{log_record["lineno"]}'
    log_record.pop('module')
    log_record.pop('funcName')
    log_record.pop('lineno')
    log_record['log_level'] = log_record['levelname'].upper()
    log_record.pop('levelname')


class LookupLogger(logging.getLoggerClass()):
  error_solutions = [
    {
      'error_match': [
        'Error code: 390101',
        'User access disabled. Contact your local system administrator'
      ],
      'suggestion': 'Someone might need to fresh auth token for service X'
    }
  ]

  def makeRecord(self, name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None):
    for check in self.error_solutions:
      for match in check['error_match']:
        if match in msg:
          extra = extra or {}
          extra['suggested_fix'] = check['suggestion']
          break
    return super().makeRecord(name, level, fn, lno, msg, args, exc_info, func, extra, sinfo)

def configure_logging(utility_name):
  logging.setLoggerClass(LookupLogger)
  c_handler = logging.FileHandler(f'{ROOT_DIR}/logs/foo.log')
  c_handler.setLevel(logging.INFO)
  log_format = '%(levelname)s %(utility)s %(module)s %(funcName)s %(lineno)d %(message)s'
  c_format = CustomJsonFormatter(fmt=log_format, utility=utility_name)
  c_handler.setFormatter(c_format)

  logging.getLogger().addHandle(c_handler)
{{< / highlight >}}
