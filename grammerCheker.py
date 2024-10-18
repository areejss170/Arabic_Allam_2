import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials


#set up the credentials
credentials =Credentials(
    url ='https://eu-de.ml.cloud.ibm.com',
    api_key ='pJ4t6ouJdAb05U5dYNJN3CjBlRdGnkz38BTY6LV0pj2E' 
)

paramaters = {
    "decoding_method":"greedy",
    "max_new_tokens":100,
    "repetition_penalty":1.0
}

model=Model(
    model_id="sdaia/allam-1-13b-instruct",
    params=paramaters,
    credentials=credentials,
    project_id='2481e389-a734-4f22-b659-6164f45ff224'
)

#start your code here , previuos code just to set up everythings 

import requests
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('pJ4t6ouJdAb05U5dYNJN3CjBlRdGnkz38BTY6LV0pj2E')
token = authenticator.token_manager.get_token()


def checker(text):


    prompt_input = f"""يتمثل دورك الأساسي في العمل كمدقق نحوي، ومساعدة المستخدمين في تصحيح الأخطاء النحوية، وتحسين بنية الجملة، وتحسين إمكانية قراءة النص بشكل عام. يجب عليك التركيز على تحديد واقتراح تصحيحات للأخطاء النحوية الشائعة، مثل أخطاء علامات الترقيم، والاستخدام غير السليم للأزمنة. مع ضمان الدقة في القواعد النحوية، يجب أيضًا أن تهدف إلى الحفاظ على الأسلوب الأصلي لكتابة المستخدم.

    أمثلة:

    النص: احب ل اخيك ما تحب ل نفسك.
    النص المصحح: أحب لأخيك ماتحب لنفسك#

    النص: يعمل مدراء المدارس على أحسن وجه.
    النص المصحح: يعمل مديرو المدارس على أحسن وجه.#

    النص:يتم جلب الفحم من المناجم.
    النص المصحح: يُجلب الفحم من المناجم#


    النص:وحدة وسيادة واستقلال البلد.
    النص المصحح: وحدة البلد وسيادته واستقلاله#

    النص: أخذ يناقش كل موضوع على حِده.
    النص المصحح: أخذ يناقش كل موضوع على حِدة#

    النص: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، ذكي الرائحة
    النص المصحح: إنه شاب حسن المظهر، متأنق في ثيابه، بهي الطلعة، زكي الرائحة#

    النص: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويزود عن شرفه يصون عرضه؟!
    النص المصحح: هل يُعاقب الحرُّ لأنه يدافع عن أرضه ويذود عن شرفه يصون عرضه؟!#


    النص: يحيى حياة لا قيمة لها ولا أمل فيها.
    النص المصحح: يحيا حياة لا قيمة لها ولا أمل فيها.#

    النص:{text}
    النص المصحح: 

    """

    generated_response = model.generate_text(prompt=prompt_input, guardrails=False)
    return (generated_response.split("#")[0])
