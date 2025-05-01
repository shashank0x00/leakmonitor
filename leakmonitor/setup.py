from setuptools import setup, find_packages

setup(
    name="leakmonitor",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests", "beautifulsoup4"],
    entry_points={
        'console_scripts': [
            'leakmonitor=leakmonitor.main:run_monitor',
        ],
    },
    author="Internal Red Team",
    description="Monitor publicly leaked credentials for your organization",
)