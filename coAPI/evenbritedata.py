from datetime import datetime

import eventbrite

from Models.Models import event_ticket, algo


class dataloader:
    oAuth = None
    event_ticket_list = list()
    eventbrite_api = None
    algo_implementation_1 = None
    algo_implementation_2 = None

    def __init__(self,oAuth):
        self.eventbrite_api = eventbrite.Eventbrite(oAuth)



        user_id = self.eventbrite_api.get_user()
        organizatino_id = self.eventbrite_api.get_organization(user_id=user_id.id)

        print(organizatino_id['organizations'])
        id_organization = [organization['id'] for organization in organizatino_id['organizations']]

        for organization_id in id_organization:
            organization_check = self.eventbrite_api.get_organization_events(organization_id=organization_id)

            events = organization_check["events"]
        organization_id = id_organization[0]
        for event in events:

            self.event_ticket_list.append(event_ticket(event['id'],organization_id))

            self.load()
            self.algo_implementation_1 = algo(10, 5, self.event_ticket_list[0], self.eventbrite_api)

            self.algo_implementation_1.incremental_algo()
        print(len(events))
    # return events_list


    def load(self):
        for event_ticket in self.event_ticket_list:
            # print(event_ticket.event_id)
            event = self.eventbrite_api.get_event(event_ticket.event_id)
            print(event)
            event_ticket.event_details(event["name"], event["url"])
            event_ticket.event_time_load(datetime.now(),datetime.strptime(event["end"]["utc"],"%Y-%m-%dT%H:%M:%SZ"))
    def load_list(self):
        list_mark = self.event_ticket_list[:2]
        return list_mark
    # def delete_tickets(self, event_id, ticket_class_id):
    #     self.eventbrite_api.delete_ticket_class(event_id,ticket_class_id)
    def load_algo(self):
        self.algo_implementation_1 = algo(10, 5, self.event_ticket_list[0], self.eventbrite_api)

        self.algo_implementation_1.incremental_algo()


def main():
    dataloader('TY4Y36NK4MF7365QHHGH')
if __name__ == "__main__":
    main()