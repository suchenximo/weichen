from zhipuai import ZhipuAI
client = ZhipuAI(api_key="ac73dba7fa003a2f04f35adf686cc90c.XyRb5XK32dEqKcr5")  # 请填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-flash",  # 请填写您要调用的模型名称
    messages=[
        {"role": "user", "content": "作为一名美食鉴赏家，请为我点的这份外卖写一段评论，评论字数不少于150字，不需要而外的东西，只需要评论即可"},
        {"role": "assistant", "content": "当然，因为要写一段外卖评论，请告诉我一些关于您所点的外卖信息"},
        {"role": "user", "content": "手撕烤鸭"}
    ],
    stream=True,
)
for message in response:    # 流式输出
    print(message.choices[0].delta.content, end="")
# print(response.choices[0].message.content)
