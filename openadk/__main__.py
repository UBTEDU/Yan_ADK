#!/usr/bin/env python

import connexion

from openadk import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Yanshee Open ADK'})
    app.run(port=10101)


if __name__ == '__main__':
    main()
