#!/usr/bin/perl
use strict;
use utf8;
use AnyEvent;
use AnyEvent::XMPP::Client;
use AnyEvent::XMPP::IM::Message;
=for licence
    <a perl script,XMPP auto reply bot, enter you $passwd,$uname, use 
    CPAN to install above packages>
    Copyright (C) <2010>  <shabi@fossix.org>

    p-reply-bot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
=cut
 
my $uname = 'lijw@ejabberd';
my $passwd = 'lijunwei';
my $server = "192.168.1.28";
my $j = AnyEvent->condvar;
my $cl = AnyEvent::XMPP::Client->new (debug => 0);
$cl->add_account ($uname,$passwd,$server);
$cl->reg_cb (
   session_ready => sub {
	my ($cl, $acc) = @_;
   	$cl->set_presence("avaliable","Under reply bot\'s control",10);
   },
   disconnect => sub {
      my ($cl, $acc, $h, $p, $reas) = @_;
      print "disconnect ($h:$p): $reas\n";
   },
   error => sub {
      my ($cl, $acc, $err) = @_;
      print "ERROR: " . $err->string . "\n";
   },
   message => sub {
      my ($cl, $acc, $msg) = @_;
	my ($u,$r) = split(/[\._@]/,$msg->from);
 	 if($msg->body()=~ /^[\s]*$/){ print $u." is typing\n";}
	else{
		$r = $msg->make_reply;
		my $rep=&sentm($msg->body,$u);
		$r->add_body($rep);
		$r->send;
		
	}
		print "$u says: ".$msg->body() . "\n";
   }
);

sub sentm{
	my $msg=shift;
	my $u =shift;
	my $reply;
	if($msg=~/([hH]ow)|([hH]i)|([hH]ey)|([Hh]ello)/){return $reply="$u, Hi.. How are you.. ";}
	if($msg=~/([Ww]hat)|\?|([Ww]at)|(^did)/){return $reply="yes but not really $u... :) ";}
	if($msg=~/([Ww]hy)|([Ww]hen)/){return $reply="may be in sometime $u.. :)";}
	if($msg=~/([Oo]kay)|([oO]k)/){return $reply="good";}
	else {return $reply="hey $u, I will alert if I meet $ENV{'USER'}";}
}	
$cl->start;
$j->wait;