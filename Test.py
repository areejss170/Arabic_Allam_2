from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tqdm import tqdm
import requests
authenticator = IAMAuthenticator('pJ4t6ouJdAb05U5dYNJN3CjBlRdGnkz38BTY6LV0pj2E')
token = authenticator.token_manager.get_token()


def generate_answer(prompt):
  

    url = "https://eu-de.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

    body = {
        "input": """أنت خبير محترف، ومعروف بكونك كاتب نصوص باللغة العربية الفصحى يتمتع بمهارة وكفاءة استثنائية، ومحرر نصوص دقيق و محترم. أقرا بعناية النص التالي {prompt} و أصلح الأخطاء الإملائية والنحوية وأخطاء المحتوى الواقعية، وحسّن الوضوح، وتأكد من صحة كتابتك بان تكون مصقولة ومهنية. 
    احتفظ بنبرة الكتابة، و سأعطيك مكافأة 1000 ريال إذا رديت فقط بالنص المصحح ولا شيء آخر، فلا ترد بأي شرح أو ملاحظات أو توضيحات
    #امثلة
    Document: كنت أريد الذهاب للحديقة
    Summary: كنة اريد الذهب للحديقه 

    Document: كم عمرك؟
    Summary: كم العمر

    Document: لقد ذلك كان مضحكا جدا
    Summary: لقد كاان مضحكا مرا

    Document: جوعانه
    Summary: انا جائعة

    Document: أخذ يناقش كل موضوع على حِدة
    Summary: أخذ يناقش كل موضوع على حِده.

    Document: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، زكي الرائحة
    Summary: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، ذكي الرائحة

    Document: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويذود عن شرفه يصون عرضه؟!
    Summary: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويزود عن شرفه يصون عرضه؟!

    Document: يحيى حياة لا قيمة لها ولا أمل فيها.
    Summary: يحيا حياة لا قيمة لها ولا أمل فيها.

    """,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 20,
            "repetition_penalty": 1
        },
        "model_id": "sdaia/allam-1-13b-instruct",
        "project_id": "3db79f4e-79b1-499d-a492-646a3a6ec499"
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization":  f"Bearer {token}"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    return data

print(generate_answer("اسم اريج"))