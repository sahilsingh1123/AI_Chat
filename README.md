# Night's Watch AI Chat

Welcome to the Night's Watch AI Chat project! This project leverages powerful AI chat models from Cohere, OpenAI, and Bard to provide an interactive chat experience.

## Features

- **Model Selection**: Users can choose between Cohere, OpenAI, or Bard AI models to power the chatbot.
- **Interactive Chat**: Engage in conversations with the AI chatbot directly through the interface.
- **Session Persistence**: Chat history is stored in the session, allowing for continuous interaction without losing context.

## How to Use

1. Select the AI chat model of your choice from the dropdown menu.
2. Enter your message into the chat input box.
3. Press "Send" to get a response from the AI.
4. Your chat history will be displayed in the interface, with messages from both you and the AI.

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set up your environment variables `COHERE_API_KEY` and `OPENAI_API_KEY` with your respective API keys.
4. Run the Streamlit application with `streamlit run home.py`.

## Dependencies

- Streamlit
- Requests
- Dotenv
- Cohere SDK
- OpenAI SDK

## API Configuration

API keys for Cohere and OpenAI should be set as environment variables. The application uses these keys to authenticate and interact with the respective AI services.

## Disclaimer

This project is for demonstration purposes only. The Bard chat model is not configured at this time.

## Contributions

Contributions to the Night's Watch AI Chat project are welcome. Please feel free to submit pull requests or open issues to discuss potential improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
