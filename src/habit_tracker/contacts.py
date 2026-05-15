import logging
from habit_tracker.logger import get_logger

logging.getLogger().setLevel(logging.DEBUG)

logger = get_logger(__name__)

contacts = {
    'number': 4,
    'students':
    [
        {
            'name': 'Alice',
            'phone': '123-456-7890',
            'email': 'alice@mail.com'
        },
        {
            'name': 'Bob',
            'phone': '234-567-8901',
            'email': 'bob@mail.com'
        },
        {
            'name': 'Charlie',
            'phone': '345-678-9012',
            'email': 'charlie@mail.com'
        },
        {
            'name': 'David',
            'phone': '456-789-0123',
            'email': 'david@mail.com'
        }
    ]
}

mails = []
for student in contacts['students']:
    mails.append(student['email'])

logger.info(f"Le email dei contatti sono: {', '.join(mails)}")