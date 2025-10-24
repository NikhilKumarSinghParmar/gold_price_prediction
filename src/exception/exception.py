'''
import sys
import os


class CustomException(Exception):
	def __init__(
		self,
		error_message,
		error_detail:sys
	):
        super.__init__(e)
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()
        self.line_no=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
		

    def __str__(self):
        return f"The exception [{0}] ,\n raised at file [{1}] ,\n at line number [{2}]".format(
            self.error_message,
            self.file_name,
            self.line_no
        )



if __name__=="__main__":
    try:
        pass

    except Exception as e:
        raise CustomException(e,sys)
'''



import sys
import os


class CustomException(Exception):
  def __init__(self, error_message, error_detail: sys):
    super().__init__(error_message)
    self.error_message = error_message
    _, _, exc_tb = error_detail.exc_info()
    self.line_no = exc_tb.tb_lineno
    self.file_name = exc_tb.tb_frame.f_code.co_filename

  def __str__(self):
    return f"The exception [{self.error_message}],\n raised at file [{self.file_name}],\n at line number [{self.line_no}]"


if __name__ == "__main__":
  try:
    a=10/0

  except Exception as e:
    raise CustomException(e, sys)



