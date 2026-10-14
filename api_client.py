
import requests

def get_data(url,headers=None):

    try:
        r=requests.get(url,
                       headers=headers,
                       timeout=10)
        r.raise_for_status()

        data=r.json()
        return{
            "success":True,
            "data":data,
            "error":None
        }
    except requests.exceptions.HTTPError as  e:
             return {
            "success": False,
            "data": None,
            "error": f"HTTP错误: {e}"
        }
    except requests.exceptions.Timeout as e:
            return {
            "success": False,
            "data": None,
            "error": f"连接超时: {e}"
            }
    except requests.exceptions.ConnectionError as e:
         return {
            "success": False,
            "data": None,
            "error": f"连接失败: {e}"
        }
    except requests.exceptions.RequestException as e:
           return {
            "success": False,
            "data": None,
            "error": f"请求错误: {e}"
        }


def post_data(url, headers=None, json=None):

    try:
        r = requests.post(
            url,
            json=json,
            headers=headers,
            timeout=10
        )

        r.raise_for_status()

        data = r.json()

        return {
            "success": True,
            "data": data,
            "error": None
        }

    except requests.exceptions.HTTPError as e:
        return {
            "success": False,
            "data": None,
            "error": f"HTTP错误: {e}"
        }

    except requests.exceptions.Timeout as e:
        return {
            "success": False,
            "data": None,
            "error": f"连接超时: {e}"
        }

    except requests.exceptions.ConnectionError as e:
        return {
            "success": False,
            "data": None,
            "error": f"连接失败: {e}"
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "data": None,
            "error": f"请求错误: {e}"
        }