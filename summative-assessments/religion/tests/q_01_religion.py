test = {
  'name': 'Question 01_religion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'religion'
          >>> 'religion' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'religion'
          >>> # from its initial state (of ...)
          >>> religion is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(religion, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> religion
                  level  rescuers  actives  bystanders
          0        Very        65        9          17
          1    Somewhat        79       17          34
          2    Not very        41       18          11
          3  Not at all        25        4          10
          4      out of       210       48          72
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
