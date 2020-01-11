'''
const class
@Author: guandao
@Date: 2020-01-12 02:57:59
@LastEditTime : 2020-01-12 03:51:14
@see : https://www.cnblogs.com/Vito2008/p/5006255.html
'''
class _const:
  
  class ConstError(TypeError): 
    pass
  
  class ConstCaseError(ConstError):
    pass
  
  def __setattr__(self, name, value):
    if name in self.__dict__.keys():
      raise self.ConstError("Can't change const.%s" % name)
    if not name.isupper():
      raise self.ConstCaseError('The const name "%s" is not all uppercase' % name)
    self.__dict__[name] = value


  def __getattr__(self, name):
    if name in self.__dict__.keys():
      return self.name
    return None


  def __delattr__(self, name):
    if name in self.__dict__:
      raise self.ConstError("Can't delete const.%s" % name)
    raise NameError(name)

import sys
sys.modules[__name__] = _const()