___
# Large Language Models in Education
___

## Table of content

1. [Introduction](#introduction)
2. [Problem and Solution](#problem-and-solution)
3. [High Level Solution Architecture](#high-level-solution-architecture)
4. [Methodology](#methodology)
5. [Conclusion](#conclusion)

## Introduction
In the last few years, artificial intelligence has advanced significantly, particularly in the fields of generative AI and large language models (LLMs). These cutting-edge models have proven to be exceptionally capable of reading, writing, and producing content that is human-like, opening up new horizons in creativity and invention. These generative AI models provide fascinating prospects in the field of education where technology integration is becoming more common. Intelligent tutoring systems have been sought after in education for a long time to improve and customize students’ learning experiences. The effectiveness of generative AI paired with the current trends in educational technology use offer a potent synergy that has the potential to completely change the educational environment.

The "Large Language Models in Education" addresses many challenges in the educational platforms. Inappropiate responses, privacy concerns, Bias & fairness, high cost, continuous improvement are some of these challenges. A major concern identified is the high cost of accessing Large Language Model APIs. As a solution, "Smart Tutor" has been developed. This cost-effective intelligent tutor focuses on reducing expenses while improving the accuracy of prompts. This prototype relies on a cache implementation with local context and a question-and-answer model to achieve cost reduction. The methodology is implemented for a specific cousre called computer architecture and this prototype can be used for other modules if similar steps are followed.

## Problem & Soultion
- Problem : High Cost of Accessing LLM APIs
- Solution : Cost Effective Intelligent Tutor
![diagram](./docs/images/problem_and_solution.PNG)

## High Level Solution Architecture
![diagram](./docs/images/high_level_architecture_diagram.PNG)

## Methodology
1. Create High Level Solution Architecture
2. Plan System Data flow
3. Collect Course Materials and Create Datasets
4. QA Model Implementation
5. Create Similarity Checker
6. Cache Implementation
7. Backend Implemenatation
8. Frontend Implemenatation
9. Integration of Implementations

## Conclusion
The deliverable of the project is a prototype which is capable of integrating with any course materials with a custom based memory (Local Context) instead of a frozen memory. This prototype has the ability of integrating any QA model, checking the accuracy and getting the highest scored answers for prompts. And finally, the number of API calls are reduced using cache, specially, because most of the time the users are asking the similar questions and because of that there will always be cache hits. From that situation, the number of API calls are reduced. 

## Team

- E/17/297, Rupasinghe T. T. V. N., [e17297@eng.pdn.ac.lk](mailto:e17297@eng.pdn.ac.lk)
- E/17/206, Manohora H. T., [e17206@eng.pdn.ac.lk](mailto:e17206@eng.pdn.ac.lk)
- E/17/148, Kalpana M. W. V., [e17148@eng.pdn.ac.lk](mailto:e17148@eng.pdn.ac.lk)

## Supervisors

- Dr. Damayanthi Herath, [damayanthiherath@eng.pdn.ac.lk](mailto:damayanthiherath@eng.pdn.ac.lk)
- Prof. Roshan G. Ragel, [roshanr@eng.pdn.ac.lk](mailto:roshanr@eng.pdn.ac.lk)
- Dr. Isuru Nawinne, [isurunawinne@eng.pdn.ac.lk](mailto:isurunawinne@eng.pdn.ac.lk)
- Dr. Shamane Siriwardhana, [gshasiri@gmail.com](mailto:gshasiri@gmail.com)

## Related Links
- [Project Page](https://cepdnaclk.github.io/e17-4yp-Large-Language-Models-in-Education/)
- [Department Website](http://www.ce.pdn.ac.lk/)

