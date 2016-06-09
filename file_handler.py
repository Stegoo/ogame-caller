import config

def write_message(message):
    f = open(config.message_file, 'w+')
    print("writing speech:", message)
    f.write(message)
    f.close()

def write_call_file(mobile_number=config.mobile_number, max_retries=5, retry_time=300, wait_time=45, context="ogame_attack_warning"):
    f = open(config.call_file, 'w+')
    f.write("Channel: SIP/%s@provider\n" % mobile_number)
    f.write("MaxRetries: %s\n" % max_retries)
    f.write("RetryTime: %s\n" % retry_time)
    f.write("WaitTime: %s\n" % wait_time)
    f.write("Context: %s\n" % context)
    f.write("Extension: %s\n" % mobile_number)
    f.write("Priority: 1\n")
    f.close()
