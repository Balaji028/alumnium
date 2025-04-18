from behave import *
from playwright.sync_api import Page
from selenium.webdriver import Chrome


@given('I open "{url}"')
def step_impl(context, url):
    if isinstance(context.driver, Chrome):
        context.driver.get(url)
    elif isinstance(context.driver, Page):
        context.driver.goto(url)


@when('I create a new task "{title}"')
def step_impl(context, title):
    context.al.do(f"create a new task '{title}'")


@when('I mark the "{title}" task as completed')
def step_impl(context, title):
    context.al.do(f'mark the "{title}" task as completed')


@when('I mark the "{title}" task as uncompleted')
def step_impl(context, title):
    context.al.do(f'mark the "{title}" task as uncompleted')


@when('I delete the "{title}" task')
def step_impl(context, title):
    context.al.do(f'delete the "{title}" task')


@when("I mark all tasks as completed")
def step_impl(context):
    # Avoid attempting to complete tasks one by one.
    context.al.do("mark all tasks as completed using 'Toggle All' button")


@when('I show only "{filter}" tasks')
def step_impl(context, filter):
    context.al.do(f'I show only "{filter}" tasks')


@when("I clear completed tasks")
def step_impl(context):
    context.al.do("clear completed tasks")


@then('"{title}" task is shown in the list of tasks')
def step_impl(context, title):
    assert title in context.al.get("titles of tasks")


@then('"{title}" task is not shown in the list of tasks')
def step_impl(context, title):
    assert title not in context.al.get("titles of tasks")


@then('"{title}" task is not marked as completed')
def step_impl(context, title):
    context.al.check(f'"{title}" task is not marked as completed')


@then('"{title}" task is marked as completed')
def step_impl(context, title):
    context.al.check(f'"{title}" task is marked as completed')


@then("tasks counter is {count:d}")
def step_impl(context, count):
    assert context.al.get("number of left items in a tasks counter") == count
