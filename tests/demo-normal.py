from llm_store.gateway import LLMGateway
from llm_store.store.baserowstore import BaseRowStore
import os

if __name__ == "__main__":
    store = BaseRowStore(
        api_host=os.environ.get("BASEROW_API_HOST", "localhost"),
        api_key=os.environ.get("BASEROW_API_KEY", ""),
        db_code="3",
        model_table_code="614",
        prompt_table_code="308",
        chat_log_table_code="309")

    llm_gateway = LLMGateway(store)
    prompt_code = "test_template"

    # -- 获取 AI 模型
    llm_model = llm_gateway.get_model(prompt_code)

    # -- 渲染 Prompt
    messages = llm_gateway.render_prompt(prompt_code, {"topic": "科幻"})

    # -- 执行对话
    chatCompletion = llm_gateway.completions(llm_model, messages, trace_id="1234567890")
    print(chatCompletion)