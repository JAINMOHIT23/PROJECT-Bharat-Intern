import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('bus_tickets')

def book_ticket(bus_number, passenger_name, seat_number):
    response = table.get_item(
        Key={
            'bus_number': bus_number,
            'seat_number': seat_number
        }
    )
    if 'Item' in response:
        return {'message': 'Seat is already taken'}
    
    table.put_item(
        Item={
            'bus_number': bus_number,
            'seat_number': seat_number,
            'passenger_name': passenger_name
        }
    )
    
    return {'message': 'Ticket booked successfully'}

def get_tickets(bus_number):
    response = table.query(
        KeyConditionExpression='bus_number = :bus_number',
        ExpressionAttributeValues={
            ':bus_number': bus_number
        }
    )
    
    tickets = []
    for item in response['Items']:
        ticket = {
            'bus_number': item['bus_number'],
            'seat_number': item['seat_number'],
            'passenger_name': item['passenger_name']
        }
        tickets.append(ticket)
        
    return {'tickets': tickets}

def lambda_handler(event, context):
    request = json.loads(event['body'])
    
    if event['resource'] == '/book_ticket':
        response = book_ticket(request['bus_number'], request['passenger_name'], request['seat_number'])
    elif event['resource'] == '/get_tickets':
        response = get_tickets(request['bus_number'])
    

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }