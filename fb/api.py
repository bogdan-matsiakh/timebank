import facebook
from models import FacebookUser

def put_wall_post(user_obj,message,reciever_obj=None,attachments={}):
    ''' pushes wall post to users facebook wall '''
    ret_dict = {'success':False,'message':''}
    try:
        access_token = FacebookUser.objects.values_list('access_token').get(user=user_obj)[0]
    except FacebookUser.DoesNotExist,e:
        ret_dict['message'] = 'user does not exists'
        return ret_dict

    if(reciever_obj):
        try:
            profile_id = FacebookUser.objects.values_list('uid').get(user=reciever_obj)[0]
        except FacebookUser.DoesNotExist,e:
            ret_dict['success'] = False
            ret_dict['message'] = 'revciever oject not found'
            return ret_dict
            
    else:
        profile_id = 'me'
    graph = facebook.GraphAPI(access_token)
    ret_message = graph.put_wall_post(message,attachment=attachments,profile_id=profile_id)
    print ret_message
    ret_dict['success'] = True
    ret_dict['message'] = 'Message Posted Successfull'
    return ret_dict

