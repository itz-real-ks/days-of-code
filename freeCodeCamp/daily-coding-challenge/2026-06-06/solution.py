from typing import Optional, List, Any, Dict

def UserProfile(username: str, posts: int, verified: bool, role: str, badges: List[str], supporter: Optional[bool] = None, **kwargs):
    ROLES = ('user', 'creator', 'moderator', 'staff', 'admin')
    # try-> Catching the invalids
    try:
        if not isinstance(username, str):
            return False

        # found isinstance(posts,Ture) & isinstance(True,int) -> true
        if not isinstance(posts, int) or isinstance(posts, bool):
            return False

        if not isinstance(verified, bool):
            return False

        if role not in ROLES:
            return False
        # badges strictly:str only not empty[]
        if not isinstance(badges, list) or not all(isinstance(badge, str) for badge in badges):
            return False

        # supporter: not None; but is bool [Optional]
        if supporter is not None and not isinstance(supporter, bool):
            return False
            
        return True
    except Exception:
        return False

# Unpacks the dict orderly
def is_valid_schema(obj: dict, **kwargs):

    if not isinstance(obj, dict) or 'users' not in obj:
        return False
        
    users = obj.get('users') # gets users from dict key
    if not isinstance(users, list):
        return False

    if not users:
        return True

    def safe_validate_user(user_data):
        if not isinstance(user_data, dict):
            return False
        try:
            return UserProfile(**user_data)
        except TypeError:

            return False
    return all(safe_validate_user(user_data) for user_data in users)
