import config

def write_message(message):
    f = open(config.message_file, 'w+')
    print("writing speech:", message)
    f.write(message)
    f.close()

def write_call_file(mobile_number=config.mobile_number, max_retries=5, retry_time=300, wait_time=45, context="ogame_attack_warning"):
    f = open(config.call_file, 'w+')
    f.write("Channel: SIP/%s@provider" % mobile_number)
    f.write("MaxRetries: %s" % max_retries)
    f.write("RetryTime: %s" % retry_time)
    f.write("WaitTime: %s" % wait_time)
    f.write("Context: %s" % context)
    f.write("Extension: %s" % mobile_number)
    f.write("Priority: 1")
    f.close()
