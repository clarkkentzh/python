#coding=utf-8
import re
str = "Django has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:Tutorials take you by the hand through a series of steps to create a Web application. Start here if you’re new to Django or Web application development. Also look at the “First steps” below.Topic guides discuss key topics and concepts at a fairly high level and provide useful background information and explanation.Reference guides contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.How-to guides are recipes. They hisDjango mdjangoaa guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume knowledge of how Django works."

a = re.compile(r'\S*Django\S*',re.I)
print a.findall(str)