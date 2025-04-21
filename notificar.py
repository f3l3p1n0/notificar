import sys                                                                                                              
import requests

def enviar_notificacion(mensaje):                                                                                           
    token = "TOKEN"                                                                
    chat_id = "CHATID"                                                                                                  
    url = f"https://api.telegram.org/bot{token}/sendMessage"                                                                
    data = {"chat_id": chat_id, "text": mensaje}                                                                            
    requests.post(url, data=data)                                                                                                                                                                                                               

if __name__ == "__main__":                                                                                                  
    mensaje = " ".join(sys.argv[1:])                                                                                        
    enviar_notificacion(mensaje)
