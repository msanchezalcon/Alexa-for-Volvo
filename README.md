# Master thesis

Master Thesis on integrating the handbook into Alexa

## See demos:
1. https://drive.google.com/file/d/1SLMRRvd68UomCXXoFC4sB7MjdOP6ZRme/view?usp=sharing
2. https://drive.google.com/file/d/1JWA65Mu5yxZrHWe0IDs2Al9Vm6H53hvx/view?usp=sharing

## Code structure

```bash
masterthesis/
├── interactionModels
│   └── custom
│       └── en-US.json
├── lambda
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── utils.py
├── README.md
└── skill.json
```

The frontend code is in **en-US.json**.
The backend code is mainly in **lambda_functions.py**. Any helper functions should be put in utils.py.
