#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts node into sorted linked list
 * @head: pointer to pointer to first node in linked list
 * @number: the number to insert into linked list
 * Return: the address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp;
	listint_t *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	for (current = *head; current && current->next; current = current->next)
	{
		if (number < current->n)
		{
			temp = *head;
			*head = new;
			new->next = temp;
			return (new->next);
		}
		else if (number < current->next->n)
		{
			temp = current->next;
			current->next = new;
			new->next = temp;
			return (new);
		}
	}
	current->next = new;
	return (current->next);
}
