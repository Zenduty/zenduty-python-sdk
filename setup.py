from setuptools import setup, find_packages

setup(
    name="zenduty-api",
    version="1.0.0",
    description="Python SDK wrapper for the Zenduty API",
    long_description="""
        # Zenduty Python SDK

        The **Zenduty Python SDK** provides a seamless way to integrate with Zenduty's powerful incident management platform. Whether you're building automated workflows, custom dashboards, or advanced monitoring solutions, this SDK offers the tools you need to connect with Zenduty's API endpoints efficiently.

        ## About Zenduty

        Zenduty is a cutting-edge incident management platform designed to help teams resolve incidents faster, smarter, and with greater ease. By leveraging advanced automation, Zenduty ensures that developers and engineers stay in control during high-pressure scenarios. Zenduty empowers teams to:

        - Proactively identify and resolve issues before they escalate.
        - Collaborate effectively to minimize downtime and service disruptions.
        - Improve reliability and customer satisfaction with actionable insights.

        ## Why Use the Zenduty Python SDK?

        The Zenduty Python SDK is crafted for developers looking to integrate their applications or services with Zenduty. It simplifies the process of interacting with Zenduty's API and supports robust and scalable integrations for a variety of use cases, including:

        - Triggering, acknowledging, and resolving incidents programmatically.
        - Accessing detailed analytics and reporting data.
        - Managing services, teams, schedules, and escalation policies.
        - Building automation pipelines for incident notifications and workflows.

        ## Key Features

        - **Ease of Use**: Intuitive methods and structures to reduce development time.
        - **Comprehensive API Support**: Full access to Zenduty's endpoints for managing incidents, teams, schedules, and more.
        - **Scalability**: Designed to handle complex workflows and high-volume environments.
        - **Compatibility**: Works seamlessly with modern Python environments and frameworks.

        ## Installation

        You can install the Zenduty Python SDK quickly via pip:

        ```sh
        $ pip install zenduty-api
        ```
        
        or you may grab the latest source code from GitHub:

        ```sh
        $ git clone https://github.com/Zenduty/zenduty-python-sdk
        ```

        ## Docs
        Please refer this link to understand the SDK better. https://github.com/Zenduty/zenduty-python-sdk
        """,
    long_description_content_type="text/x-rst",
    author="Javeed Yara",
    author_email="javeed@zenduty.com",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "urllib3==2.2.2",
        "six==1.9.0",
        "charset-normalizer==3.3.2",
        "idna==3.7",
        "certifi==2024.7.4",
        "regex==2024.11.6",
    ],
    url="https://github.com/Zenduty/zenduty-python-sdk",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",  # Update based on your package's status
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",  # Specify Python versions supported
    ],
    python_requires=">=3.9",  # Specify the minimum Python version
    scripts=["bin/client.py"],  # Include any scripts you want to make executable
)
