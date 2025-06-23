test = {
  'name': 'Question 03_rescuers_actives',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'rescuers_actives'
          >>> 'rescuers_actives' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'rescuers_actives'
          >>> # from its initial state (of ...)
          >>> rescuers_actives is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(rescuers_actives)
          ['rescuers', 'actives']
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> rescuers_actives
                      rescuers  actives
          level                        
          Very              65        9
          Somewhat          79       17
          Not very          41       18
          Not at all        25        4
          """,
          'hidden': False,
          'locked': False
        },
        #: end-extra
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
