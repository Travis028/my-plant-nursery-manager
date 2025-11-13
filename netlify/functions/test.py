def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': '''
        <!DOCTYPE html>
        <html>
        <head><title>Test Function</title></head>
        <body>
            <h1>Netlify Function Test</h1>
            <p>If you see this, Netlify functions are working!</p>
            <a href="/.netlify/functions/app">Go to Main App</a>
        </body>
        </html>
        '''
    }