#!/usr/bin/env python3

import firebase_admin
from firebase_admin import messaging, credentials

cred = credentials.Certificate("certificate.json")
firebase_admin.initialize_app(cred)


registration_token = 'dlxkdy1_SZ6Th0GQd9iYml:APA91bEIsJ-GuNtPfL9D3WMptShSKXJWxnCOBUV-BZvhL5FziB0bLncVtIp6kPxgMhHn-UDQwRMyIgl4lgAbZs1Qf5I3G43XG_RTBO0uj3_1-EzPlHc2KwNfupjcn5krqIydPrB2XVmH'

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': '1000',
        'time': '3:45',
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
