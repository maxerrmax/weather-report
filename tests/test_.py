# test_weather.py
import random
import re
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from weather import weather_report

def test_weather_sunny(monkeypatch):
    monkeypatch.setattr(random, "choice", lambda _: "sunny")
    monkeypatch.setattr(random, "randint", lambda a, b: 30) 

    report = weather_report("Barcelona")

    assert "sunny" in report
    assert "Barcelona" in report
    assert "30 degrees" in report

def test_weather_snowing(monkeypatch):
    monkeypatch.setattr(random, "choice", lambda _: "snowing")
    monkeypatch.setattr(random, "randint", lambda a, b: -5)

    report = weather_report("Oslo")

    assert "snowing" in report
    assert "Oslo" in report
    assert "-5 degrees" in report

def test_weather_other(monkeypatch):
    monkeypatch.setattr(random, "choice", lambda _: "cloudy")
    monkeypatch.setattr(random, "randint", lambda a, b: 15)

    report = weather_report("London")

    assert "cloudy" in report
    assert "London" in report
    assert "15 degrees" in report
