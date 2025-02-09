test = {
  'name': 'Question 01_titanic',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'titanic'
          >>> 'titanic' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'titanic'
          >>> # from its initial state (of ...)
          >>> titanic is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(titanic, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        #: begin-extra
        {
          'code': r"""
          >>> titanic.head().loc[:, :'age']
                                       name  gender   age
          0             Abbing, Mr. Anthony    male  42.0
          1       Abbott, Mr. Eugene Joseph    male  13.0
          2     Abbott, Mr. Rossmore Edward    male  16.0
          3  Abbott, Mrs. Rhoda Mary 'Rosa'  female  39.0
          4     Abelseth, Miss. Karen Marie  female  16.0
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
