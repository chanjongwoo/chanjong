from slacker import Slacker

token = "xoxb-135797385811-933250460480-Yl5z76aaCNNiSRP4x2rnWJXq" # 종봇
#token = "xoxb-135797385811-935194805424-sld7lHzgzmnEawz0nV4mmj2T" # 데참이

slack = Slacker(token)
slack.chat.post_message('mkt_naver_sa_auto_alert', '무언가를 시작하는 방법은 말하는 것을 멈추고 행동을 하는 것이다.', as_user=True)
#slack.chat.post_message('mkt_signup_alert', 'test', as_user=True)
