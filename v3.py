from whatsapp_v2 import whatsapp_v2
class w_v3(whatsapp_v2):
    def call(self):
        print('calling')
w=w_v3()
w.