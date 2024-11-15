import os

from llm_store.gateway import LLMGateway
from llm_store.store.baserowstore import BaseRowStore

if __name__ == "__main__":
    store = BaseRowStore(
        api_host=os.environ.get("BASEROW_API_HOST", "localhost"),
        api_key=os.environ.get("BASEROW_API_KEY", ""),
        db_code="3",
        model_table_code="614",
        prompt_table_code="308",
        chat_log_table_code="309")
    llm_gateway = LLMGateway(store)

    # 不使用远程 Prompt 模式
    messages = [{"role": "system", "content": "今天星期几"}]

    # -- 获取 模型信息
    model_code = "litellm-us"
    model_record = llm_gateway.get_model(model_code)

    # -- 执行对话
    chatCompletion = llm_gateway.completions(model_record, messages, trace_id="1234567890")
    print(chatCompletion)