from typing import Any, List, Optional

from expand_langchain.chain.llm import llm_chain
from expand_langchain.utils.parser import parser_chain
from expand_langchain.utils.registry import chain_registry
from expand_langchain.utils.sampling import sampling_chain
from langchain_core.runnables import RunnableLambda
from langfuse.decorators import langfuse_context, observe


@chain_registry(name="cot")
def cot_chain(
    key: str,
    examples: Optional[dict] = None,
    n=1,
    **kwargs,
):
    async def _func(data, config={}):
        chain = llm_chain(
            examples=list(examples.values()),
            **kwargs,
        )
        input_prompt = chain.get_prompts()[0][-1].format(**data).content
        # if input prompt is not str, apply .to_string()
        if not isinstance(input_prompt, str):
            input_prompt = input_prompt.to_string()

        parser = parser_chain(**kwargs)
        result = await chain.ainvoke(data, config=config)
        parsed_result = parser.invoke(result, config=config)

        return {
            f"{key}_input": input_prompt,
            f"{key}_raw": result,
            key: parsed_result,
        }

    chain = RunnableLambda(_func)

    result = sampling_chain(chain, n, **kwargs)
    result.name = key

    return result
