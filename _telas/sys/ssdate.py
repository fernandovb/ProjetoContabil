from _telas.desingner.tssdate import TSSDATE


class SSDATE(TSSDATE):
    date = ''

    def __init__(self, *args, **kwargs):
        super(SSDATE, self).__init__(*args, **kwargs)
        self.fc_retorna_data()

    def ac_day(self, event):
        self.dp_data.Value = self.cl_calendario.PyGetDate()
        self.fc_retorna_data()

    def ac_month(self, event):
        self.dp_data.Value = self.cl_calendario.PyGetDate()
        self.fc_retorna_data()

    def ac_year(self, event):
        self.dp_data.Value = self.cl_calendario.PyGetDate()
        self.fc_retorna_data()

    def ac_data_change(self, event):
        self.cl_calendario.SetDate(self.dp_data.Value)
        self.fc_retorna_data()

    def fc_retorna_data(self):
        fdate = self.cl_calendario.PyGetDate()
        self.date = fdate.strftime('%d/%m/%Y')
