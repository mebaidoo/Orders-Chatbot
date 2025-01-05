import re
from rasa.engine.graph import GraphComponent, ExecutionContext
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.engine.recipes.default_recipe import DefaultV1Recipe
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.training_data.training_data import TrainingData
from rasa.shared.nlu.constants import ENTITIES
from typing import Any, Dict, List, Text

# @DefaultV1Recipe.register([GraphComponent], is_trainable=False)
@DefaultV1Recipe.register(component_types=[DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR], is_trainable=False)
class CustomEntityExtractor(GraphComponent):
    def __init__(self, config: Dict[Text, Any]) -> None:
        self.keywords = config.get("keywords", {})
        self.number_range = config.get("number_range", (1, 50))
        self.regex_patterns = config.get("regex_patterns", {})

    def train(self, training_data: TrainingData) -> None:
        pass

    def process(self, messages: List[Message]) -> List[Message]:
        for message in messages:
            entities = []
            text = message.get("text").lower()

            # Handle keyword matching
            for entity_type, keywords in self.keywords.items():
                for keyword in keywords:
                    if keyword in message.get("text").lower():
                        entities.append({
                            "start": message.get("text").lower().find(keyword),
                            "end": message.get("text").lower().find(keyword) + len(keyword),
                            "value": keyword,
                            "entity": entity_type
                        })

            # Extract numbers within the specified range
            for match in re.finditer(r'\b\d+\b', text):
                number = int(match.group())
                if self.number_range[0] <= number <= self.number_range[1]:
                    entities.append({
                        "start": match.start(),
                        "end": match.end(),
                        "value": match.group(),
                        "entity": "number_in_range"
                    })

            # Handle regular expression matching
            for entity_type, patterns in self.regex_patterns.items():
                for pattern in patterns:
                    for match in re.finditer(pattern, text):
                        entities.append({
                            "start": match.start(),
                            "end": match.end(),
                            "value": match.group(),
                            "entity": entity_type
                        })

            message.set(ENTITIES, message.get(ENTITIES, []) + entities)

        print(messages)
        return messages

    @classmethod
    def create(cls, config: Dict[Text, Any], execution_context: ExecutionContext) -> GraphComponent:
        return cls(config)