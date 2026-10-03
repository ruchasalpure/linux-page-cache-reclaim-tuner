from crewai import Agent

linux_page_cache_reclaim_tuner = Agent(
    role="Linux Page Cache Reclaim Tuner",
    goal="Deliver high-precision autonomous Linux Page Cache Reclaim Tuner operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
