import constants as c
import helpers


def run():
   ip_list = helpers.open_log_file(c.REG_EX)
   
   helpers.write_to_csv(c.OUTPUT_FILE, ip_list) 


if __name__ == '__main__':
    run()