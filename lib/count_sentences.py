#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value
      
  @property
  def value(self):
    return self._value
    
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    if(self.value[len(self.value) - 1] == '.'):
      return True
    else:
      return False
  
  def is_question(self):
    if(self.value[len(self.value) - 1] == '?'):
      return True
    else:
      return False
      
  def is_exclamation(self):
    if(self.value[len(self.value) - 1] == '!'):
      return True
    else:
      return False
      
  def count_sentences(self):
    #Checing an empty string
      if len(self.value) == 0:
        print(len(self.value))
        return len(self.value)
      
      if self.value[len(self.value) - 1] == '?':
        self.value = self.value.replace('?', '', -1)
      else:
        self.value = self.value.replace('?', '.')
        
      if self.value[len(self.value) - 1] == '!':
        self.value = self.value.replace('!', '', -1)
      else:
        self.value = self.value.replace('!', '.')
      
      print(self.value)
      new_list = self.value.rsplit('.')
      new_list = set(new_list)
      
      if '' in new_list:
         new_list.remove('')
         
      print(new_list)
      print(len(new_list))
      return len(new_list)
          
empty_string = MyString()
simple_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
empty_string.count_sentences()