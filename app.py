from services.service import RequesterService

if __name__ == '__main__':
    requester = RequesterService()
    result = requester.extract()
    print(result)
