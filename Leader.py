from flask import Flask,request
import requests,json
app=Flask(__name__)
@app.route('/')
def owner():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <link rel="shortcut icon" href="https://www.linkpicture.com/q/IMG_20211223_210042_106.jpg"/>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#343a40" />
  <meta
          name="description"
          content="Links To My Accounts | Developed By - Ahmed!"
  />  
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
     <title>‽</title>
     <style>
       body{
         background-color:#BCBCBC ;
       }
       h5{
             color: #343a40;
       }
       .name{
           color: #343a40;
       }
       .love{
           color: #343a40 !important;
       }
       /*----------------- Mail-------------------- */
       #email{
           text-decoration: none;
           float: right;
           color:#343a40;
       }
       .footer{
           margin-top: 5% !important;
           margin-bottom: 10px;
       }
       @media (max-width: 479px) {
            .footer{
            margin-top: 35% !important;
            }
       }
     </style>
</head>
<body>
<div class="container">
  <div class="media mt-5">
    <img src="https://www.linkpicture.com/q/IMG_20211223_210042_106.jpg" class="m-3" alt="image" width="75px" height="75px">
    <div class="media-body m-2">
      <h5 class="align-items-center mt-2">Ahmed‽</h5>
      <p>Hey I'm Just Devolpoer !.</p>
      <p>My official accounts below </p>
    </div>
  </div>
<div class="mt-4">
  <a href="https://github.com/aazo" class="btn btn-outline-dark btn-block" role="button" target="_blank"><i class="fab fa-github">&nbsp;</i>Github</a>
  <br>
  <a href="#" class="btn btn-outline-dark btn-block" role="button" target="_blank"><i class="fab fa-codepen">&nbsp;</i>Codepen</a>
  <br>
  <a href="https://Instagram.com/u.ryy" class="btn btn-outline-dark btn-block" role="button" target="_blank"><i class="fab fa-instagram">&nbsp;</i>Instagram</a>
  <br>
  <a href="https://mobile.twitter.com/bl_ee" class="btn btn-outline-dark btn-block" role="button" target="_blank"><i class="fab fa-twitter">&nbsp;</i>Twitter</a>
  <br>
  <a href="https://t.me/Noelx" class="btn btn-outline-dark btn-block" role="button" target="_blank"><i class="fab fa-telegram">&nbsp;</i>Telegram</a>
</div>
        <!--------------------Footer---------------------------->
  <div class="footer mt-5">
    <hr/>
    <h6>Made With <span class="love">🖤</span> in Baghdad, Iraq 🇮🇶</h6>
    <h6>
      Proudly Hosted By
      <a href="/" class="name" target="_blank"> Ahmed! </a>
      <a id="email" href="mailto: iahmedai90@gmail.com"> <i class="fa fa-envelope"> </i> </a>
    </h6>
  </div>
</div>
</body>
  
</html>'''
@app.route('/api/tele')
def tele():
    user= request.args.get('user')
    r=requests.get(f'https://t.me/{user}')
    if 'https://telegram.org/img/t_logo.png' in r.text:
        rq='Not Taken'
    else:
        rq='Taken'
    data1={'data':rq,'status':'loaded','owner':'noelx'}
    data_x=json.dumps(data1)
    try:
        return data_x
    except:pass
@app.route('/api/ip')
def ip():
    ips=request.access_route[-1]
    data_ip={'ip':ips}
    ij=json.dumps(data_ip)
    return ij

