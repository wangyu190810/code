###达拉然(dalaran)
后台权限控制


+ 用户管理

+ 权限管理

+ 权限构建



用户只能使用甜品邮箱作为自己的登录账户

###接口
    url: /api/check_perm
    method: GET
    params:
        user_id 用户id，
        action  请求的权限点
    
    return 1 拥有权限
           0 没有权限
           
    
    