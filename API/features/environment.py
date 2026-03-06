def after_all(context):
    if not context.failed:
        print("\nAll tests passed")
    else:
        print("\nSome validations failed. Please check the assertion errors above.")