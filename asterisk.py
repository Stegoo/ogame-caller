import config
import file_handler
import shutil

def call(msg=config.default_message):
    #write the message to open by the call file and read by the tts engine (Flite)
    file_handler.write_message(msg)
    #copy the call file into asterisk folder for outgoing call
    #copy permissions but not meta data, consider using shutil.copy2 if you need them
    file_handler.write_call_file()
    shutil.copy(config.call_file, config.asterisk_outgoing)
